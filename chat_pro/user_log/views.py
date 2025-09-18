from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.http import HttpResponse
from django.contrib import messages
from .models import UserSignup
# Create your views here.
def user_log(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully signed up")
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'log/signup.html', {"form": UserSignupForm()})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserSignup.objects.filter(username=username, password=password)
        if user:
            request.session['username'] = username
            messages.success(request, "Login successful")
        else:
            # Here you would typically check the username and password against the database
            messages.error(request, "Invalid username or password")
    return render(request, 'log/login.html')

def profile_view(request):
    username = request.session.get('username')
    if not username:
        messages.error(request, "You must be logged in to view the profile.")
        return redirect('login')

    try:
        user = UserSignup.objects.get(username=username)
    except UserSignup.DoesNotExist:
        messages.error(request, "User does not exist.")
        return render(request, 'log/login.html')

    return render(request, 'log/profile.html', {"user": user})