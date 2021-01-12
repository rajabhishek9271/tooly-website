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
