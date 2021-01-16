from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.views.generic.detail import DetailView
from django.template.loader import render_to_string

from recruiter.models import Job, Company
from django.contrib.auth.models import User
from . import models
from .forms import UserForm

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import MustBeApplicantMixin
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError

# from .filters import JobTitleFilter


# Create your views here.

class HomePage(View):
    def get(self, request, *args, **kwargs):
        curr_jobs = models.Job.objects.all().order_by('-id')[:10]
        curr_companies = Company.objects.all().order_by('-id')[:10]

        context = {
            'curr_jobs':curr_jobs,
            'curr_companies':curr_companies
        }
        return render(request, 'index.html', context)


    def post(self, request, *args,**kwargs):

        form = request.POST
        country = form.get('country')
        keyword = form.get('keyword')

        request.session['country'] = country
        request.session['keyword'] = keyword

        return redirect('applicant:jobs_list')


class AboutPage(TemplateView):
    template_name = "about.html"

class ErrorPage(TemplateView):
    template_name = "404.html"

class ApplicationsPage(LoginRequiredMixin, MustBeApplicantMixin, View):

    login_url='/accounts/login/'
    def get(self, request, *args, **kwargs):

        curr_user = request.user
        curr_applicant = models.Applicant.objects.get(user=curr_user)

        applications = models.Application.objects.filter(
            applicant=curr_applicant
        ).order_by('-id')

        p = Paginator(applications,10)
        page_no = request.GET.get('page',1)
        applications = p.page(page_no)


        index = applications.number - 1
         # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
        max_index = len(p.page_range)
    # You want a range of 7, so lets calculate where to slice the list
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
        page_range = list(p.page_range)[start_index:end_index]

        # jobs = Job.objects.all()
        context = {
            'applications':applications,
            'page_range': page_range

        }
        return render(request, 'applications.html', context)

class DashboardPage(LoginRequiredMixin, MustBeApplicantMixin, View):

    login_url='/accounts/login/'
    def get(self, request, *args, **kwargs):

        curr_user = request.user
        curr_applicant = models.Applicant.objects.get(user=curr_user)

        applications = models.Application.objects.filter(
            applicant=curr_applicant
        ).order_by('-id')[:5]  # TAKE ONLY THE 5 MOST RECENT APPLICATIONS

        p = Paginator(applications,10)
        page_no = request.GET.get('page',1)
        applications = p.page(page_no)


        index = applications.number - 1
         # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
        max_index = len(p.page_range)
    # You want a range of 7, so lets calculate where to slice the list
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
        page_range = list(p.page_range)[start_index:end_index]

        # jobs = Job.objects.all()
        context = {
            'applications':applications,
            'page_range': page_range

        }
        return render(request, 'dashboard.html', context)

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


class JobListingPage(View):
    def get(self, request, *args, **kwargs):

        try:
            keyword = request.session['keyword']
            country = request.session['country']
        except KeyError:
            # If user did'nt search anything and pressed search button
            keyword = ""
            country = ""
            jobs = Job.objects.all()

        form = request.GET
        job_title = form.get('title', '')
        job_type = form.get('type', '')
        job_edu = form.get('edu', '')

        # Get code from keyword
        keyword_list = keyword.split(", ")
        code = keyword_list[-1][4:]

        if country == "United States of America":
            jobs = Job.objects.filter(company__country=country, onet_codes__contains=code)
        elif country == "Canada":
            jobs = Job.objects.filter(company__country=country, noc_codes__contains=code)

        # Additional filters from get request
        jobs = jobs.filter(
            job_title__icontains=job_title,
            job_type__contains=job_type,
            education_level__contains=job_edu

        )

        total_results = jobs.count()
        p = Paginator(jobs,10)
        page_no = request.GET.get('page',1)
        jobs = p.page(page_no)


        index = jobs.number - 1
         # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
        max_index = len(p.page_range)
    # You want a range of 7, so lets calculate where to slice the list
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
        page_range = list(p.page_range)[start_index:end_index]
        # f = JobTitleFilter(request.GET, queryset=Job.objects.all())
        context = {
        'jobs':jobs,
        'keyword':keyword,
        'page_range': page_range,
        'title': job_title,
        'job_type':job_type,
        'job_edu':job_edu,
        'total_results':total_results
        # 'filter':f

        }


        return render(request, "job-listing.html", context=context)

    def post(self, request, *args,**kwargs):

        form = request.POST

        keyword = form.get('keyword')

        request.session['keyword'] = keyword

        return redirect('applicant:jobs_list')


class JobDetailView(DetailView):

    context_object_name ='job_detail'
    model = Job
    template_name = 'job-details.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        job_id = self.kwargs['pk']
        job = Job.objects.get(id=job_id)
        applicant = models.Applicant.objects.get(user=user)

        try:
            application = models.Application.objects.create(
            applicant=applicant,
            applied_job=job,
            )
            application.save()
        except IntegrityError:
            messages.warning(request, "You have already applied to this job! You can check its status in the Dashboard")
            return redirect('applicant:home')

        messages.success(request, "Your Application has been submited! You can check its status in the Dashboard")
        return redirect('applicant:home')


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



                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)


        # This is the render and context dictionary to feed
        # back to the registration.html file page.
        messages.success(request, "You have been successfully registered.")
        return redirect('applicant:home')

class MessagePage(TemplateView):
    template_name = "message.html"

class OrderPage(TemplateView):
    template_name = "orders.html"

class PricingPage(TemplateView):
    template_name = "pricing.html"

class ProductDetailsPage(TemplateView):
    template_name = "product-details.html"

class ProfilePage(LoginRequiredMixin, MustBeApplicantMixin, View):
    login_url = '/accounts/login/'

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
    messages.success(request, "You have been logged out.")

    return redirect('applicant:home')


def delete_user(request):
    if request.method == 'POST':
        User.objects.filter(id=request.user.id).delete()
        messages.info(request, "Your Account has been successfully deleted.")
        return redirect('applicant:home')
    else:
        return redirect('applicant:home')



class ResumeProfilePage(TemplateView):
    template_name = "resume-profile.html"

class ReviewsPage(TemplateView):
    template_name = "reviews.html"

class ShopPage(TemplateView):
    template_name = "shop.html"

class BookmarkPage(TemplateView):
    template_name = "bookmarks.html"


def handler404(request, exception):

    return render(request, 'errors/404.html')



def handler403(request, exception):

    return render(request, 'errors/403.html')
