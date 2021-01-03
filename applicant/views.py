from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from recruiter.models import Job, Company
from django.contrib.auth.models import User
from django.contrib.auth import logout
from . import models
from django.contrib.auth.decorators import login_required
from .forms import UserForm
# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

    def post(self, request, *args,**kwargs):

        form = request.POST

        keyword = form.get('keyword')

        request.session['keyword'] = keyword

        return redirect('recruiter:jobs_list')


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

# @login_required(login_url='profile.html')
class ProfilePage(View):
    def get(self, request, *args, **kwargs):

        new_user = models.Applicant.objects.get(
            user = request.user
        )

        context = {
        'new_user':new_user
        }


        return render(request, 'profile.html', context=context)


    def post(self, request, *args, **kwargs):

        data = request.POST
        user = request.user
        profile_pic = data.get('profile_pic')
        # resume = form.get('myFile')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = int(data.get('phone'))
        address1 = data.get('address-one')
        address2 = data.get('address-two')
        country = data.get('country')
        zipcode = data.get('zipcode')
        new_password = data.get('new-password')
        confirm_password = data.get('confirm-password')

        new_applicant = models.Applicant.objects.get(
            user = request.user
        )

        new_applicant.phone_no=phone
        new_applicant.address_line1=address1
        new_applicant.address_line2=address2
        new_applicant.country=country
        new_applicant.zipcode=zipcode

        new_applicant.save()


        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if(new_password != " "):
            user.set_password(new_password)

        user.save()

        # new_applicant.profile_pic=profile_pic,
        return render(request, 'index.html')


        # def delete_view(request, id):
        # # dictionary for initial data with
        # # field names as keys
        #     context ={}
        #
        # # fetch the object related to passed id
        # obj = get_object_or_404(Applicant, username = username)
        #
        #
        # if request.method =="POST":
        #     # delete object
        #     obj.delete()
        #     # after deleting redirect to
        #     # home page
        #     return HttpResponseRedirect("/")
        #
        # return render(request, "profie.html", context)

def logout_view(request):
    logout(request)
    return redirect('applicant:home')



class ResumeProfilePage(TemplateView):
    template_name = "resume-profile.html"

class ReviewsPage(TemplateView):
    template_name = "reviews.html"

class ShopPage(TemplateView):
    template_name = "shop.html"

class WishlistPage(TemplateView):
    template_name = "wishlist.html"
