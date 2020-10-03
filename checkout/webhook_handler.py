from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .models import Order, OrderLineItem
from events.models import EventInstance
from results.models import Result
from profiles.models import UserProfile, AthleteProfile

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        """  SEND THIS IF ORDER EXISTS BELOW OR IF CREATED BY WEBHOOK HANDLER"""

        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        


    def _create_result(self, order, event):
        """Create a result in the database"""
        """  CREATE THIS IF ORDER EXISTS BELOW OR IF CREATED BY WEBHOOK HANDLER"""
        print('This will create a result for the following order:')
        print(order)
        intent = event.data.object
        cart = intent.metadata.cart
        
        # Decide if this is myself or a Racehub Friend
        # Calculate the age category
        # Create the new result
        # EITHER USER ATHLETE PROFILE DATA OR USE SAVED NON RACEHUB FRIENDS DATA
        for item_id, item_data in json.loads(cart).items():
            eventpurchased = EventInstance.objects.get(id=item_id)
            # Get the athlete_profile data for each item in the cart
            for athlete, quantity in item_data['items_by_athlete'].items():
                order_line_item = OrderLineItem(
                    order=order,
                    event=eventpurchased,
                    quantity=quantity,
                    which_athlete=athlete,
                )
                print('This is the order data')
                print(order_line_item)
                print('Athlete:')
                print(order_line_item.which_athlete)
                print('Event:')
                print(order_line_item.event)
                print('----')
                athleteidforthisresult = order_line_item.which_athlete.split("#")
                print('----')
                print(athleteidforthisresult[1])
                selectedathleteid = athleteidforthisresult[1]
                print('----')
                selectedathletetoenter = AthleteProfile.objects.get(id=athleteidforthisresult[1])
                print('-- create a result for: --')
                print(selectedathletetoenter.athletefirstname)
                print(selectedathletetoenter.athletesurname)
                print(selectedathletetoenter.gender)
                print(selectedathletetoenter.dateofbirth)
                print(selectedathletetoenter.club)
                print(selectedathletetoenter.id)
                print('-- at this event: --')
                print(order_line_item.event.friendlyname)
                print(order_line_item.event.id)
                newresult = Result.objects.create(
                    eventinstance = order_line_item.event,
                    athletefirstname = selectedathletetoenter.athletefirstname,
                    athletesurname = selectedathletetoenter.athletesurname,
                    dateofbirth = selectedathletetoenter.dateofbirth,
                    gender = selectedathletetoenter.gender,
                    club = selectedathletetoenter.club,
                )
                # get the result just created, make the bib number equal to the id number and resave.
                # get the result just created, generate an age category and resave
                
               

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()


        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            print ('ORDER EXISTS SO CREATE A RESULT NOW')
            self._create_result(order, event)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    eventpurchased = EventInstance.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            eventpurchased=eventpurchased,
                            quantity=item_data,
                        )
                        
                        order_line_item.save()
                    else:
                        for athlete, quantity in item_data['items_by_athlete'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                event=eventpurchased,
                                quantity=quantity,
                                which_athlete=athlete,
                            )
                            
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        print ('I am going to add a row to the Results database for this order now...')
        self._create_result(order, event)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Payment Failed Webhook received: {event["type"]}',
            status=200)