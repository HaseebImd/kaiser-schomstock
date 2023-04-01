from django.contrib import admin
from .models import Jobs, JobImages


class AdminJobs(admin.ModelAdmin):
    list_display = ['postTitle','createdat']

class AdminJobImages(admin.ModelAdmin):
    list_display = ['jobObject','image']

admin.site.register(Jobs, AdminJobs)
admin.site.register(JobImages, AdminJobImages)
# Register your models here.
