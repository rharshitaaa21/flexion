from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.Home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.user_login, name="login"),
    path('about', views.about, name="about"),
    path('logout', views.user_logout, name="logout"),
    path('contact', views.contact, name="contact"),
    path('enroll', views.enroll, name="enroll"),
    path('profile', views.profile, name="profile"),
    path('gallery', views.gallery, name="gallery"),
    path('services', views.services, name="services"),
    path('attendence', views.attendence, name="attendence"),

]
