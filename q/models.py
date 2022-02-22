from django.db import models
from q.models import *

# Create your models here.

class Register_model(models.Model):
    fname = models.CharField(max_length=250)
    mname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    username = models.CharField(max_length=250,unique=True)
    phone = models.BigIntegerField(unique=True)
    rephone = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=254,unique=True)
    reemail = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=150)
    repassword = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    city = models.CharField(max_length=100)


class Login_model(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=150)


class Contact_model(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    phone = models.BigIntegerField()
    desc = models.CharField(max_length=4141)