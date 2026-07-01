from django.shortcuts import render
from django.http import HttpResponse
from .models import User_data
# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username == "" or email == "" or password == "":
            return HttpResponse("Please fill all the fields")
        elif User_data.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        elif len(password) < 8:
            return HttpResponse("Password must be at least 8 characters long")
        else:
            user = User_data(name=username, email=email, password=password)
            user.save()
    return render(request, 'signup.html')
# cross site request forgery

def login(request):
    return render(request, 'index.html')

def home(request):
    users = User_data.objects.all()
    return render(request, 'index.html', {'users': users, 'role':"student"})

def profile(request, id):
    user = User_data.objects.get(id=id)
    return render(request, 'profile.html', {'user': user})


def profile_del(request, id):
    user = User_data.objects.get(id=id)
    user.delete()
    return HttpResponse("User deleted successfully")

def profile_update(request, id):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User_data.objects.get(id=id)
        user.name = username
        user.email = email
        user.password = password
        user.save()

    return render(request, "update.html")
