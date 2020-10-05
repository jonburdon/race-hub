from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

from .models import UserProfile, AthleteProfile, RaceHubFriends, NonRaceHubFriends
from results.models import Result
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    athleteprofile = get_object_or_404(AthleteProfile, user=request.user)
    currenttime = datetime.datetime.now()
    print ('My USERNAME is:')
    print (profile)
    myusername = profile
    print(athleteprofile.id)
    print (myusername)
    racehubfriends = RaceHubFriends.objects.all()
    # Needs to Filter to match if the value 'rfuserprofile' is equal to 'athleteprofile' This should work!! See line 43 below - this would match the data perfectly.
    racehubfriendsforthisathlete = racehubfriends.filter(rfuserprofile_id=athleteprofile.id)  
    nonracehubfriends = NonRaceHubFriends.objects.all()
    nonracehubfriendsforthisathlete = nonracehubfriends.filter(parentprofile_id=athleteprofile.id)
    allresults = Result.objects.all()
    resultsforthisathlete = allresults.filter(linkedathlete=athleteprofile.id)
    
      
   # print ('Athlete ID:')
   # print (athleteprofile.id)
   # print ('All Non Racehub Friends:')
   # for friend in nonracehubfriends:
   #     print (friend.athletefirstname)
   #     print (friend.athletesurname)
   #     print("_______")
   # print("_______")
   # print ('Non Racehub Friends for this athlete:')
   # for friend in nonracehubfriendsforthisathlete:
   #     print (friend.athletefirstname)
   #     print (friend.athletesurname)
   #     print("_______")
   # print("_______")
    print ('Athlete ID:')
    print (athleteprofile.id)
    print ('Racehub Friends:')
    print (racehubfriends)
    for friend in racehubfriends:
        print ('My Username:')
        print (myusername)
        print ('My Data to match:')
        print (friend.rfuserprofile)
        if myusername == friend.rfuserprofile:
            print ('Owner Profile')
            print (friend.rfuserprofile)
            print (friend.rfuserprofile_id)
            print ('Athlete Profile')
            print (friend.myfriendsracehubid)
        
        
        print("_______")
        
    print ('Racehub Friends for this athlete:')
    print (racehubfriendsforthisathlete)
    for friend in racehubfriendsforthisathlete:
        print (friend.rfuserprofile)
        
       

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'athleteprofile': athleteprofile,
        'racehubfriends': racehubfriends,
        'resultsforthisathlete': resultsforthisathlete,
        'racehubfriendsforthisathlete': racehubfriendsforthisathlete,
        'nonracehubfriendsforthisathlete': nonracehubfriendsforthisathlete,
        'on_profile_page': True,
        'currenttime': currenttime
    }

    return render(request, template, context)

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)