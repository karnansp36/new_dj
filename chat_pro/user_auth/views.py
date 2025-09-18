from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup
# Create your views here.
def home(request):
    users = Signup.objects.all()
    users = []
    return render(request, 'auth/index.html', {"users": users})


def about(request):
    return render(request, 'auth/about.html')

def signup(request):
    if request.method == "POST":
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')

       if username == "" or email == "" or password == "":
           return HttpResponse("All fields are required")
       else:
           Signup.objects.create(username=username, email=email, password=password)
           return HttpResponse("successfully signed up")
           
    return render(request, 'signup.html')