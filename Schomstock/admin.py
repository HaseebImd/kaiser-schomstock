from django.contrib import admin
from .models import ZipCodeLatLong


class AdminZipCodeLatLong(admin.ModelAdmin):
    list_display = ['zipCode','lat','long']

admin.site.register(ZipCodeLatLong, AdminZipCodeLatLong)

# Register your models here.
