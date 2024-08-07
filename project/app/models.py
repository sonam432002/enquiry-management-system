from django.db import models

# Create your models here.
class RegData(models.Model):
 name=models.CharField(max_length=50)
 lname=models.CharField(max_length=50)
 password=models.CharField(max_length=50)
 contact=models.IntegerField()
 email=models.EmailField()

class Enquiry(models.Model):
 name=models.CharField(max_length=50)
 lname=models.CharField(max_length=50)
 password=models.CharField(max_length=50)
 contact=models.IntegerField()
 email=models.EmailField()
 enquiry=models.CharField(max_length=70)

class AdminReg(models.Model):
 name=models.CharField(max_length=50)
 lname=models.CharField(max_length=50)
 password=models.CharField(max_length=50)
 contact=models.IntegerField()
 email=models.EmailField()
