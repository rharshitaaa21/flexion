from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def Home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['usernumber']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('signup')

        myUser = User.objects.create_user(name, email, pass1)
        myUser.save()
        messages.success(request, "User is created successfully")
        return redirect('login')
          
    return render(request, "signup.html")

def user_login(request):
    return render(request, "login.html")