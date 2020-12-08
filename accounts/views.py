from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        # Register user
        #messages.error(request, 'Testing error message')
        # return redirect('register')

        # GET FORM values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # check duplicate username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "Username already taken, Try again with different username")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, "Email already exits, Try Login")
                    return redirect('register')
                else:
                    # Create user
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'User successfully registered, Try Login')
                    return redirect('login')
        else:
            messages.error(request, "Those Passwords didn't match, Try again")
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
