from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact, MembershipPlan, Trainer, Enrollment
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


def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('login')


def contact(request):
    if request.method == "POST":
        name = request.POST['fullname']
        email = request.POST['email']
        number = request.POST['num']
        desc = request.POST['desc']
        myquery = Contact(name= name, email = email, phonenumber = number, description = desc)
        myquery.save()

        messages.info(request, "Thanks for contacting us, We will get back to you soon!")
        return redirect('contact')

    else:
        return render(request, "contact.html")
    

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"You need to Login first")
        return redirect('login')
    Membership= MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    context = {"Membership": Membership, "SelectTrainer": SelectTrainer,}
    if request.method == 'POST':
        FullName = request.POST.get('Fullname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        PhoneNumber = request.POST.get('PhoneNumber')
        DOB = request.POST.get('DOB')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        reference = request.POST.get('reference')
        address = request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request, "Thank You for Enrolling!")
        return redirect('enroll')

    return render(request, "enroll.html", context)
