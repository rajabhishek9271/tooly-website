from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from .forms import RecruiterForm
from .models import Company, Job
from django.http import JsonResponse


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



        keyword = request.session['keyword']
        jobs=Job.objects.filter(job_title__contains=keyword)

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




        print("returning from view")
        context = {
        'jobs':jobs,
        'keyword':keyword
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

class CompanyDetailView(DetailView):
    context_object_name = 'company'
    model = Company
    template_name = 'employer_detail.html'


class PostJobView(TemplateView):
    template_name = 'post_job.html'
