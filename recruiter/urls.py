from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RecruiterRegisterPage.as_view(), name="recruiter_register"),
    path('jobs_list/<int:pk>/',views.JobDetailView.as_view(),name='job_detail'),
    path('jobs_list/', views.JobListingPage.as_view(),name='jobs_list'),
    ]
