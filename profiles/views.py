from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .forms import AddRacehubFriendForm, FamilyandFriendsForm, AthleteProfileForm

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
    racehubfriendsforthisathlete = racehubfriends.filter(rfathleteprofile_id=athleteprofile.id)
    racehubfriendprofiles = AthleteProfile.objects.all()
    
    nonracehubfriends = NonRaceHubFriends.objects.all()
    nonracehubfriendsforthisathlete = nonracehubfriends.filter(parentprofile_id=athleteprofile.id)
    allresults = Result.objects.all()
    resultsforthisathlete = allresults.filter(linkedathlete=athleteprofile.id)
    
      
    
    for friend in racehubfriendsforthisathlete:
        print (friend.myfriendsracehubid)
        
       

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
        'racehubfriendprofiles': racehubfriendprofiles,
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

@login_required
def add_racehub_friend(request):
    """ Add a racehub friend to Myracehub """
    template = 'profiles/add_racehub_friend.html'
    athleteprofile = get_object_or_404(AthleteProfile, user=request.user)
    racehubfriends = RaceHubFriends.objects.all()
    if request.method == 'POST':
        form = AddRacehubFriendForm(request.POST, request.FILES)
        if form.is_valid():
            print('Here is the form data')
            for f in form:
                print(f)
                athletetoadd = str(f)
                athletetoadd = athletetoadd.split('value="')
                finalathleteid=athletetoadd[1].split('"')
                myracehubfriendsid = finalathleteid[0]
                print ('This is the friends id')
                print (myracehubfriendsid)
                # Check an athlete profile exists with this id number
                athleteadded=False
                for r in racehubfriends:
                    print ('test-----')
                    print (r.id)
                    print (myracehubfriendsid)
                    if int(myracehubfriendsid) == int(r.id):
                        print ('Valid athlete found')
                        newresult = RaceHubFriends.objects.create(
                            rfathleteprofile = athleteprofile,
                            myfriendsracehubid = myracehubfriendsid,
                        )
                        athleteadded=True
                    else:
                        print ('No match')
                if athleteadded:
                    messages.success(request, 'Friend successfully added to My Racehub!')
                else:
                    messages.warning(request, 'That was not a valid Racehub Athlete ID. Valid numbers are displayed at the top of your friends My Racehub Profile page. Add Friends and Family for non Racehub Athletes!')
                
            context = {
            'form': form,
    }
            return render(request, template, context)
        else:
            messages.error(request, 'Failed to add Racehub friend. Please ensure the form is valid.')
    else:
        form = AddRacehubFriendForm()
        
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_nonracehubfriend(request):
    """ Add non racehub friend to My Racehub """


    if request.method == 'POST':
        form = FamilyandFriendsForm(request.POST, request.FILES)
        if form.is_valid():
            event=form.save()
            messages.success(request, 'Successfully added athlete! They will be saved on your My Racehub profile, and you can now enter them for Racehub events.')
            return redirect(reverse('event_profile', args=[event.id]))
        else:
            messages.error(request, 'Failed to add athlete. Please ensure the form is valid.')
    else:
        form = FamilyandFriendsForm()


    template = 'profiles/add_non_racehub_friend.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def add_athlete_profile(request):
    """ Add an athleteprofile to My Racehub """

    if request.method == 'POST':
        form = AthleteProfileForm(request.POST, request.FILES)
        if form.is_valid():
            athleteprofile=form.save()
            messages.success(request, 'Successfully added athlete profile!')
            return redirect(reverse('my_racehub'))
        else:
            messages.error(request, 'Failed to add profile. Please ensure the form is valid.')
    else:
        form = AthleteProfileForm()


    template = 'profiles/add_athlete_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)