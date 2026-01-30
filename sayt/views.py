from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PasswordChangeForm,CustomUserRegistrationForm,ContactForm,ChangeProfileForm



from .models import HomePage,AboutPage,Blog,Profile





def home(request):
    home = HomePage.objects.filter(is_active=True).first()
    about = AboutPage.objects.filter(is_active=True).first()
    blogs = Blog.objects.filter(is_active=True)
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/#contact')




    context = {
        'home': home,
        'about': about,
        'blogs': blogs,
        'form': form,
    }
    return render(request,'index.html', context)





def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = CustomUserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    home = HomePage.objects.filter(is_active=True).first()
    context = {
        'form': form,
        'home': home,
    }
    return render(request, 'register.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'home')
    home = HomePage.objects.filter(is_active=True).first()
    context = {
        'form': form,
        'home': home,
    }

    return render(request, 'login.html', context)




def logout_view(request):
    home=HomePage.objects.filter(is_active=True).first()
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    context = {
        'home': home,
    }

    return render(request, 'logout.html',context)


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    home = HomePage.objects.filter(is_active=True).first()
    context = {
        'profile': profile,
        'home': home,
    }
    return render(request, "profile.html", context)






def blog(request, pk):
    home = HomePage.objects.filter(is_active=True).first()
    article = get_object_or_404(Blog, pk=pk, is_active=True)


    ctx = {
        'home': home,
        'blog': article,
    }
    return render(request, 'blog-single.html', ctx)


@login_required
def profile_change(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    home = HomePage.objects.filter(is_active=True).first()
    if request.method == "POST":
        form = ChangeProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            user = request.user
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get('full_name')
            if username:
                user.username = username
            if email:
                user.email = email
            if full_name:
                user.full_name = full_name
                user.first_name = full_name
            user.save()
            messages.success(request, "Profil yangilandi ✅")
            return redirect("profile")
    else:
        form = ChangeProfileForm(instance=profile)

    context = {
        'form': form,
        'home': home,
        'profile': profile,
    }
    return render(request, "profile-change.html", context)

@login_required
def change_password(request):
    home = HomePage.objects.filter(is_active=True).first()
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form,
        'home': home,
    }
    return render(request, 'change-password.html', context)

