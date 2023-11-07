from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return f"{self.name} {self.email}"
    

class Enrollment(models.Model):   
         
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='M')
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(default=0)
    DueDate=models.DateTimeField(blank=True,null=True)
    joiningDate=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return f"{self.FullName}{self.Email}{self.PhoneNumber}{self.SelectMembershipplan} {self.SelectTrainer}"
    

class Trainer(models.Model):
    
    name=models.CharField(max_length=55)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='M')

    phone=models.CharField(max_length=25)   
    salary=models.IntegerField()
    joiningDate=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f"{self.name}{self.phone}{self.salary}{self.joiningDate}"
    

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField()

    def __int__(self):
        return f"{self.plan} {self.price}"
    


class Gallery (models.Model):
    title = models.CharField(max_length=100)
    addedtime = models.DateTimeField(auto_now_add=True, blank= False)
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return f"{self.title}"
    