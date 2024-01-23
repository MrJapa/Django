from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import timedelta
from .models import CustomUser

# Create your views here.
def index(request):
    return render(request, 'index.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(timedelta(days=14))
            else:
                request.session.set_expiry(0)

            return redirect('index')  # Adjust as per your index/home view
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        address_type = request.POST['address_type']
        door_number = request.POST['door_number']

        # Add validation logic here

        # Creating a new user instance
        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            address_type=address_type,
            door_number=door_number
        )
        user.save()

        messages.success(request, 'Account created successfully')
        return redirect('login')  # Redirect to login page after signup
    return render(request, 'signup.html')

def success_view(request):
    return render(request, 'success.html')