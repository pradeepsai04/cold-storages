from django.urls import path
from . import views
urlpatterns=[
 path('',views.page1,name='home'),
 path('next',views.next,name='next'),
 path('register',views.register,name='register'),
 path('nextonline',views.nextonline,name='nextonline')
]