from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return f"{self.name} {self.email}"
    