from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'recruiter'
urlpatterns = [
    path('register/', views.RecruiterRegisterPage.as_view(), name="recruiter_register"),
    path('post_job/', views.PostJobView.as_view(), name='post_job'),
    path('employer_detail/<int:pk>/', views.CompanyDetailView.as_view(),name='employer_detail'),
    path('recruiter_home/', views.RecruiterHomePage.as_view(),name='home'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
