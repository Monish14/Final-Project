from django.urls import path
from hello import views


#Giving the name of fuction which we want to use
urlpatterns = [
    path("", views.home, name="home"),
]