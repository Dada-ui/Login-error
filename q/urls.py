from q import views
from django.urls import path

urlpatterns = [
    path('',views.cover,name='cover'),
    path('home',views.home,name='home'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('contact',views.contactview,name='contact'),
    path('login',views.loginview,name='login'),
    path('register',views.registerview,name='register'),
    path('logout',views.logoutview,name='logout'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
    path('account',views.accountview,name='account'),
]