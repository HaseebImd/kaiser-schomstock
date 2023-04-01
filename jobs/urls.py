from django.urls import path
from Schomstock import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [

    path('all-jobs', AllJobs.as_view(), name='all-jobs'),
    path('create-new-job', NewJob.as_view(), name='create-new-job'),
    
    
    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)