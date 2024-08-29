from django.urls import path 
from provider.views import signup

urlpatterns = [
    path("signup" , signup) ,
]