from django.contrib import admin
from django.urls import path
from . import views

app_name = 'recruiter'
urlpatterns = [
    path('register/', views.RecruiterRegisterPage.as_view(), name="recruiter_register"),
    path('jobs_list/<int:pk>/',views.JobDetailView.as_view(),name='job_detail'),
    path('jobs_list/', views.JobListingPage.as_view(),name='jobs_list'),
    path('post_job/', views.PostJobView.as_view(), name='post_job'),
    path('employer_detail/<int:pk>/', views.CompanyDetailView.as_view(),name='employer_detail'),

    ]
