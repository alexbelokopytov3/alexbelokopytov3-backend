from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import Login, Registration, UserEdit, ProfileEdit
from .models import Profile
from home.views import HomeView

def Authentication(request):

    if request.method == 'POST':
        if 'sign_in' in request.POST:
            form = Login(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        # return HttpResponse('Authenticated successfully')
                        return redirect(HomeView)
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        elif 'sign_up' in request.POST:
            reg_form = Registration(request.POST)
            if reg_form.is_valid():
                # Create a new user object but avoid saving it yet
                new_user = reg_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(reg_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                profile = Profile.objects.create(user=new_user)
                return redirect(HomeView)
    else:
        reg_form = Registration()
        form = Login()
    return render(request, 'authentication/authentication.html', {'form': form, 'reg_form': reg_form})


@login_required
def Logout(request):
    logout(request)
    return redirect('HomeView')

@login_required
def Edit(request):
    if request.method == 'POST':
        user_form = UserEdit(instance=request.user, data=request.POST)
        profile_form = ProfileEdit(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('Edit')
    else:
        user_form = UserEdit(instance=request.user)
        profile_form = ProfileEdit(instance=request.user.profile)
        return render(request, 'profile/edit_profile.html', {'user_form':user_form, 'profile_form':profile_form})
