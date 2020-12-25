from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RecruiterRegisterPage.as_view(), name="recruiter_register")
]
