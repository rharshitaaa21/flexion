from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def user_login(request):
    return render(request, "login.html")