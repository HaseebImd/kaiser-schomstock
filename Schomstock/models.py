from django.db import models

# Create your models here.
class ZipCodeLatLong(models.Model):
    zipCode = models.TextField()
    lat     = models.TextField()
    long    = models.TextField()
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)

