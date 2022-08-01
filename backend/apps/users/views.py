from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import Login, Registration
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
                return redirect(HomeView)
    else:
        reg_form = Registration()
        form = Login()
    return render(request, 'authentication/authentication.html', {'form': form, 'reg_form': reg_form})


# def Authentication(request):
#     if request.method == 'POST':
#         reg_form = Registration(request.POST)
#         if reg_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return redirect(HomeView)
#     else:
#         reg_form = Registration()
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     # return HttpResponse('Authenticated successfully')
#                     return redirect(HomeView)
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = Login()
#     return render(request, 'authentication/authentication.html', {'form': form, 'reg_form': reg_form})


# def Register(request):
#     if request.method == 'POST':
#         reg_form = Registration(request.POST)
#         if reg_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return redirect(HomeView)
#     else:
#         reg_form = Registration()
#     return render(request, 'authentication/authentication.html', {'user_form': user_form})


# def Authentication(request):
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     # return HttpResponse('Authenticated successfully')
#                     return redirect(HomeView)
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = Login()
#     return render(request, 'authentication/authentication.html', {'form': form})


# Create your views here.

