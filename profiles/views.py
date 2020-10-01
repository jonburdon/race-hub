from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile, AthleteProfile, RaceHubFriends, NonRaceHubFriends
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    athleteprofile = get_object_or_404(AthleteProfile, user=request.user)
    
    racehubfriends = RaceHubFriends.objects.all()
    racehubfriendsforthisathlete = racehubfriends.filter(rfathleteprofile_id=athleteprofile.id)

    nonracehubfriends = NonRaceHubFriends.objects.all()
    nonracehubfriendsforthisathlete = nonracehubfriends.filter(parentprofile_id=athleteprofile.id)
    print ('Athlete ID:')
    print (athleteprofile.id)
    print ('All Non Racehub Friends:')
    for friend in nonracehubfriends:
        print (friend.athletefirstname)
        print (friend.athletesurname)
        print("_______")
    print("_______")
    print ('Non Racehub Friends for this athlete:')
    for friend in nonracehubfriendsforthisathlete:
        print (friend.athletefirstname)
        print (friend.athletesurname)
        print("_______")
    print("_______")
  #  print ('Athlete ID:')
   # print (athleteprofile.id)
    #print ('Racehub Friends:')
    #print (racehubfriends)
    #for friend in racehubfriends:
    #    print (friend.rfuserprofile)
    #    print (friend.rfuserprofile_id)
    #    print (friend.rfathleteprofile)
    #    print (friend.rfathleteprofile_id)
    #    
    #    print("_______")
        
    #print ('Racehub Friends for this athlete:')
   # print (racehubfriendsforthisathlete)
    #for friend in racehubfriendsforthisathlete:
     #   print (friend.rfuserprofile)
      #  print (friend.rfuserprofile_id)
       # print (friend.rfathleteprofile)
       # print (friend.rfathleteprofile_id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'athleteprofile': athleteprofile,
        'racehubfriends': racehubfriends,
        'racehubfriendsforthisathlete': racehubfriendsforthisathlete,
        'nonracehubfriendsforthisathlete': nonracehubfriendsforthisathlete,
        'on_profile_page': True
    }

    return render(request, template, context)

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