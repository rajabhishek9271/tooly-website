from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # representative_position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=300)
    company_logo = models.ImageField(upload_to='companies/logos', blank=True, null=True)
    company_description = models.CharField(max_length=1000)
    company_website = models.URLField(blank=True, null=True)
    employees_number = models.CharField(max_length=50, blank=True, null=True)
    company_email = models.EmailField()
    source = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    address = models.CharField(max_length=500)
    pincode = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = "Companies"


    def imageURL(self):
        try:
            url = self.company_logo.url
        except(e):
            url = ''
            print(e)
        return url

    def __str__(self):
        return self.company_name



class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=1000)
    job_type = models.CharField(max_length=100, default="Full Time")
    job_category = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    expires_on = models.DateTimeField(blank=True, null=True)
    education_level = models.CharField(max_length=100)
    vaccancies = models.IntegerField(blank=True, null=True)
    no_of_applicants = models.IntegerField(blank=True, null=True)
    salary = models.BigIntegerField()
    skills = models.CharField(max_length=300)
    about_job = models.CharField(max_length=800)
    keywords = models.CharField(max_length=300)
    experience = models.CharField(max_length=100)
    extra_description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} -> {self.company.company_name}"

    def get_skills(self):
        return self.skills.split(", ")

    def get_category(self):
        return self.job_category.split(", ")


# TODO: Check its functionality
    def is_expired(self):
        now = datetime.now()
        if(now >= self.expires_on):
            return True
        else:
            return False
