from django.urls import path
from Schomstock import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from . import views
urlpatterns = [

    path('all-jobs', AllJobs.as_view(), name='all-jobs'),
    path('all-jobs/job-category/<slug:jobType>', JobByCategory.as_view(), name='all-jobs/job-category'),
    path('create-new-job', NewJob.as_view(), name='create-new-job'),
    path('jobs/job-details/<int:id>', views.PostDetails, name='jobs/job-details'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('logout', views.Logout, name='logout'),
    path('job-preview', JobPreview.as_view(), name='job-preview'),
    path('all-jobs/job-search', views.JobSearch, name='job-search'),
    path('jobs/job-details/<int:job_id>/share', views.share_job, name='share_job')


    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)