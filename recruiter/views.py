from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from .forms import RecruiterForm
from .models import Company, Job
from django.http import JsonResponse
from django.core.paginator import Paginator
from . import models
from applicant.models import Application, Applicant
from django.contrib import messages
from django.db import IntegrityError



# Create your views here.


class RecruiterRegisterPage(View):


    def get(self, request, *args, **kwargs):
        user_form = RecruiterForm()
        return render(request, 'recruiter_register.html', {'form':user_form})

    def post(self, request, *args, **kwargs):
        registered = False
        if request.method == "POST":


            company_form = RecruiterForm(data=request.POST)
            form_data = request.POST

            # Check to see both forms are valid
            if company_form.is_valid():

                # Save User Form to Database
                company = company_form.save()

                # Hash the password
                company.set_password(company.password)

                # Update with Hashed password
                company.save()

                new_company = Company.objects.create(
                    user = company,
                    company_name = form_data.get('company_name'),
                    company_description = form_data.get('description'),
                    company_email = form_data.get('email'),
                    company_website = form_data.get('website'),
                    employees_number = form_data.get('no_of_emps'),
                    source = form_data.get('source'),
                    country = form_data.get('country'),
                    pincode = form_data.get('zipcode'),
                    address = form_data.get('address'),
                    phone_no = form_data.get('phone'),
                )

                new_company.save()

                registered = True

        return render(request,'index.html')


class JobListingPage(View):
    def get(self, request, *args, **kwargs):

        try:
            keyword = request.session['keyword']
        except KeyError:
            keyword = ""
        jobs=Job.objects.filter(job_title__contains=keyword)

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

        # jobs = Job.objects.all()

        if request.is_ajax():
            exp = request.GET.get('exp')
            jobs=Job.objects.filter(job_title__contains=keyword)
            total_ids=[]
            for job in jobs:
                total_ids.append(job.id)

            if exp == ">5":
                ids=[]
                jobs=Job.objects.filter(job_title__contains=keyword).filter(experience__gte=5)
                for job in jobs:
                    ids.append(job.id)

                context = {
                    'ids':ids,
                    'total_ids':total_ids
                }
                print("returning from ajax")
                return JsonResponse(context)

        context = {
        'jobs':jobs,
        'keyword':keyword,
        'page_range': page_range
        }


        return render(request, "job-listing.html", context=context)

    def post(self, request, *args,**kwargs):

        form = request.POST

        keyword = form.get('keyword')

        request.session['keyword'] = keyword

        return redirect('recruiter:jobs_list')


class JobDetailView(DetailView):

    context_object_name ='job_detail'
    model = Job
    template_name = 'job-details.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        job_id = (request.path[-2])
        job = models.Job.objects.get(id=job_id)
        applicant = Applicant.objects.get(user=user)

        try:
            application = Application.objects.create(
            applicant=applicant,
            applied_job=job,
            )
            application.save()
        except IntegrityError:
            messages.warning(request, "You have already applied to this job! You can check its status in the Dashboard")
            return redirect('applicant:home')

        messages.success(request, "Your Application has been submited! You can check its status in the Dashboard")
        return render(request, 'index1.html')

class CompanyDetailView(DetailView):
    context_object_name = 'company'
    model = Company
    template_name = 'employer_detail.html'

class PostJobView(TemplateView):
    template_name = 'post_job.html'

    def post(self, request, *args,**kwargs):

        form = request.POST
        company = models.Company.objects.get(
            user = request.user
        )
        new_job = models.Job.objects.create(
                company = company,
                job_title = form.get('job_title'),
                job_description = form.get('job_description'),
                job_type = form.get('job_type'),
                job_category = form.get('job_category'),
                education_level = form.get('education_level'),
                posted_on = form.get('posted_on'),
                vaccancies = form.get('vaccancies'),
                no_of_applicants = form.get('no_of_applicants'),
                salary = form.get('salary'),
                skills = form.get('skills'),
                about_job = form.get('about_job'),
                keywords = form.get('keywords'),
                experience = form.get('experience'),

        )
        new_job.save()
        print(form.get('job_title'))

        return render(request,'index.html')


class RecruiterHomePage(TemplateView):
    template_name = 'index1.html'
