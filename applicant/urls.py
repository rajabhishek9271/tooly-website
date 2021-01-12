from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings




app_name = 'applicant'

handler404 = views.handler404
handler403 = views.handler403

urlpatterns = [
    path('', views.HomePage.as_view(),name='home'),
    path('about/', views.AboutPage.as_view(),name='about'),
    path('404/', views.ErrorPage.as_view(),name='error'),
    path('applications/', views.ApplicationsPage.as_view(),name='applications'),
    path('blogs_detail/', views.BlogdetailsPage.as_view(),name='blogs_detail'),
    path('candidate_detail1/', views.CandidatedetailsPage.as_view(),name='candidate_detail1'),
    path('candidate_detail2/', views.CandidatedetailsTwoPage.as_view(),name='candidate_detail2'),##
    path('candidates_list/', views.CandidatelistingPage.as_view(),name='candidates_list'),##
    path('cart/', views.CartPage.as_view(),name='cart'),
    path('checkout/', views.CheckoutPage.as_view(),name='checkout'),
    path('contact/', views.ContactPage.as_view(),name='contact'),
    path('dashboard/', views.DashboardPage.as_view(),name='dashboard'),
    path('employers_list/', views.EmployerListingPage.as_view(),name='employers_list'),##
    path('faq/', views.FaqPage.as_view(),name='faq'),
    path('follows/', views.FollowsPage.as_view(),name='follows'),
    path('job_alert/', views.JobAlertsPage.as_view(),name='job_alert'),
    path('jobs_maps/', views.JobwithMapPage.as_view(),name='jobs_maps'),##
    path('register/', views.RegisterPage.as_view(),name='register'),
    path('message/', views.MessagePage.as_view(),name='message'),
    path('order/', views.OrderPage.as_view(),name='order'),
    path('pricing/', views.PricingPage.as_view(),name='pricing'),
    path('product_detail/', views.ProductDetailsPage.as_view(),name='product_detail'),
    path('profile/', views.ProfilePage.as_view(),name='profile'),
    path('resume_profile/', views.ResumeProfilePage.as_view(),name='resume_profile'),
    path('reviews/', views.ReviewsPage.as_view(),name='reviews'),
    path('shop/', views.ShopPage.as_view(),name='shop'),
    path('bookmarks/', views.BookmarkPage.as_view(),name='bookmarks'),
    path('jobs_list/<int:pk>/',views.JobDetailView.as_view(),name='job_detail'),
    path('jobs_list/', views.JobListingPage.as_view(),name='jobs_list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
