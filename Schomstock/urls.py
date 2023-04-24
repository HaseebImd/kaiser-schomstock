from django.urls import path
from Schomstock import views
from django.conf.urls.static import static
from django.conf import settings
from .views import Test,AllZipCodes
urlpatterns = [
    path("", views.Home, name="Home"),
    path('test', Test.as_view(), name='test'),
     path('all-zip-codes', AllZipCodes.as_view(), name='all-zip-codes'),
    # path("DynamicProgramming", views.DynamicProgramming, name="DynamicProgramming"),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)