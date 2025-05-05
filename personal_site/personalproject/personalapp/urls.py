from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('portfolio/',views.home,name='portfolio'),
    path('register/',views.register,name='register'),
]