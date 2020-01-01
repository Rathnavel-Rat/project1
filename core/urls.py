from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('upload/create',views.one,name="one"),
path('upload/update',views.get,name='update'),
path('upload/edit',views.edit,name="edit"),
path('upload/dash',views.dash,name="dash"),
    
    ]
