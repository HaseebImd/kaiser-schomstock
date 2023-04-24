from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from tinymce import models as tinymce_models
# Create your models here.

class Jobs(models.Model):

    city            = models.CharField(max_length=255) 
    category        = models.CharField(max_length=255)
    postTitle       = models.TextField()
    Neighborhood    = models.TextField()
    postalCode      = models.CharField(max_length=15)
    description     = tinymce_models.HTMLField()

    employementType = models.CharField(max_length=255)
    direct_contact_recureters= models.BooleanField(default=False)
    internship      = models.BooleanField(default=False)
    non_prof_org    = models.BooleanField(default=False)
    relo_ass_available = models.BooleanField(default=False)
    telecommuting   = models.BooleanField(default=False)

    jobTitle        = models.TextField()
    compensation    = models.TextField() 
    companyName     = models.TextField(blank=True, null=True)

    email           = models.CharField(max_length=255)
    emailPrivacy    = models.CharField(max_length=255)
    
    phoneCallOk     = models.BooleanField(default=False)
    smsOk           = models.BooleanField(default=False)
    showPhoneNumber = models.BooleanField(default=False)
    phoneNumber     = models.CharField(max_length=255,blank=True, null=True)
    contactName     = models.CharField(max_length=255,blank=True, null=True)

    showAddress     = models.BooleanField(default=False)
    streetName      = models.CharField(max_length=255,blank=True, null=True)
    crossStreet     = models.CharField(max_length=255,blank=True, null=True)
    cityAddress     = models.CharField(max_length=255,blank=True, null=True)

    status          = models.BooleanField(default=False)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)


class JobImages(models.Model):
    image = models.ImageField(upload_to='upload/jobs/')
    jobObject = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)


