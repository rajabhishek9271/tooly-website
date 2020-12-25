from django.shortcuts import render
from django.views.generic import View, TemplateView
from recruiter.models import Job, Company
from django.contrib.auth.models import User
from . import models
from .forms import UserForm
# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class ErrorPage(TemplateView):
    template_name = "404.html"

class ApplicationsPage(TemplateView):
    template_name = "applications.html"

class BlogdetailsPage(TemplateView):
    template_name = "blog-details.html"

class CandidatedetailsTwoPage(TemplateView):
    template_name = "candidate-details-two.html"

class CandidatedetailsPage(TemplateView):
    template_name = "candidate-details.html"

class CandidatelistingPage(TemplateView):
    template_name = "candidate-listing.html"

class CartPage(TemplateView):
    template_name = "cart.html"

class CheckoutPage(TemplateView):
    template_name = "checkout.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

class DashboardPage(TemplateView):
    template_name = "dashboard.html"

class EmployerDetailsTwoPage(TemplateView):
    template_name = "employer-details-two.html"

class EmployerDetailsPage(TemplateView):
    template_name = "employer-details.html"

class EmployerListingPage(TemplateView):
    template_name = "employerlisting.html"

class FaqPage(TemplateView):
    template_name = "faq.html"

class FollowsPage(TemplateView):
    template_name = "follows.html"

class JobAlertsPage(TemplateView):
    template_name = "job-alerts.html"

class JobDetailsTwoPage(TemplateView):
    template_name = "job-details-two.html"

class JobDetailsPage(TemplateView):
    template_name = "job-details.html"

class JobListingPage(View):
    def get(self, request, *args, **kwargs):

        jobs = Job.objects.all()

        context = {
            'jobs':jobs
        }

        return render(request, "job-listing.html", context=context)

class JobwithMapPage(TemplateView):
    template_name = "job-with-map.html"

class RegisterPage(View):
    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        return render(request, 'register.html', {'form':user_form})


    def post(self, request, *args, **kwargs):

        registered = False

        if request.method == 'POST':


            user_form = UserForm(data=request.POST)


            # Check to see both forms are valid
            if user_form.is_valid():

                # Save User Form to Database
                user = user_form.save()

                # Hash the password
                user.set_password(user.password)

                # Update with Hashed password
                user.save()

                new_applicant = models.Applicant.objects.create(

                    user = user
                )

                new_applicant.save()

                # Registration Successful!
                registered = True

        # This is the render and context dictionary to feed
        # back to the registration.html file page.
        return render(request,'index.html')

class MessagePage(TemplateView):
    template_name = "message.html"

class OrderPage(TemplateView):
    template_name = "orders.html"

class PricingPage(TemplateView):
    template_name = "pricing.html"

class ProductDetailsPage(TemplateView):
    template_name = "product-details.html"

class ProfilePage(TemplateView):
    template_name = "profile.html"


    def post(self, request):

        form = request.POST
        user = request.user
        profile_pic = form.get('profile_pic')
        # resume = form.get('myFile')
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        email = form.get('email')
        phone = form.get('phone')
        address1 = form.get('address-one')
        address2 = form.get('address-two')
        country = form.get('country')
        zipcode = form.get('zipcode')
        new_password = form.get('new-password')
        confirm_password = form.get('confirm-password')

        new_applicant = models.Applicant.objects.get(
            user = request.user

        ).update(
            # new_applicant.resume=resume,
            phone=phone,
            address1=address1,
            address2=address2,
            country=country,
            zipcode=zipcode,
        )

        new_applicant.save()

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if(new_password != " "):
            user.set_password(new_password)

        user.save()

        # new_applicant.profile_pic=profile_pic,






class ResumeProfilePage(TemplateView):
    template_name = "resume-profile.html"

class ReviewsPage(TemplateView):
    template_name = "reviews.html"

class ShopPage(TemplateView):
    template_name = "shop.html"

class WishlistPage(TemplateView):
    template_name = "wishlist.html"
