from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def Home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('signup')

        myUser = User.objects.create_user(username=phone,email= email, password=
         pass1)
        myUser.fullname = name
        myUser.save()
        messages.success(request, "User is created successfully")
        return redirect('login')
          
    return render(request, "signup.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['usernumber']
        pass1 = request.POST['pass1']
        myUser = authenticate(username=username, password=pass1)
        print(myUser)

        if myUser is not None:
            login(request, myUser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, "login.html")