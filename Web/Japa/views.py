from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from datetime import timedelta

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if remember_me:
                # Set session expiry time to a longer duration (e.g., 2 weeks)
                request.session.set_expiry(timedelta(days=14))
            else:
                # Session expires at browser close
                request.session.set_expiry(0)

            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Add validation logic here
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully')
        return redirect('login')  # Redirect to login page after signup
    return render(request, 'signup.html')

def success_view(request):
    return render(request, 'success.html')