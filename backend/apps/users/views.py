from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import Login, Registration, UserEdit, ProfileEdit
from .models import Profile
from home.views import HomeView
from home.models import Post

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
def User_delete_form(request, id):
    return render(request, 'profile/delete.html')

@login_required
def User_delete(request, id):
    user = User.objects.get(id=id)
    if request.user == user:
        logout(request)
        user.delete()
        return redirect('HomeView')
    else:
        return redirect('HomeView')

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
        return render(request, 'profile/edit.html', {'user_form':user_form, 'profile_form':profile_form})


def Profile_view(request, id):
    user_ = get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=user_)
    objects = Post.objects.filter(author_post=id).order_by('-create_date_post')
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'profile/view.html', {'page': page, 'posts': posts, 'user_': user_, 'profile': profile})