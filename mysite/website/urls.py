from django.urls import path
from . import views
urlpatterns = [
     path('',views.index,name='index'),
     path('about',views.about,name='about'),
      path('contact',views.contact,name='contact'),
      path('users',views.users,name='users'),
      path('signup',views.signup,name='signup'),
]
