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
            print(user[0].id)
            request.session['id'] = user[0].id
            messages.success(request, "Login successful")
        else:
            # Here you would typically check the username and password against the database
            messages.error(request, "Invalid username or password")
    return render(request, 'log/login.html')

def profile_view(request):
    username = request.session.get('id')
    if not username:
        messages.error(request, "You must be logged in to view the profile.")
        return redirect('login')

    try:
        user = UserSignup.objects.get(id=username)
    except UserSignup.DoesNotExist:
        messages.error(request, "User does not exist.")
        return render(request, 'log/login.html')

    return render(request, 'log/profile.html', {"user": user})



def profile_update(request, id):
    # user_data = request.session.get('username')
    # print(user_data, user.username)
    # if user_data ==  user.username:
    user = UserSignup.objects.get(id = id)
    form = UserSignupForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
        form.save()
       
    return render(request, 'log/signup.html', {"form" : UserSignupForm(instance=user)})







def explore_profile(request):
    users = UserSignup.objects.all()
    if not users:
        messages.error(request, 'profile is empty')

    return render(request, 'explore.html', {'users':users})



def read_profile(request, id):
    user = UserSignup.objects.get(id = id)
    return render(request, 'log/profile.html', {'user':user} )