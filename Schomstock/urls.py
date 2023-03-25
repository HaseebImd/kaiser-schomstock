from django.urls import path
from Schomstock import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.Home, name="Home"),
    # path("DynamicProgramming", views.DynamicProgramming, name="DynamicProgramming"),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)