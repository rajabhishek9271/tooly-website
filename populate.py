import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tooly_proj.settings')

# Setting up django configurations
import django
django.setup()

# python libraries for creating fake data
import random
from faker import Faker

from recruiter.models import Job, Company
from django.contrib.auth.models import User

def get_data():

    fakegen = Faker()

    JOB_TYPE=('Full Time', 'Part Time', 'Remote')
    EDUCATION_LEVEL=('High School', 'Graduate', 'Post Graduate')
    SALARY=(10000, 15000, 20000, 30000, 50000, 5000, 25000, 2500, 35000)
    SKILLS=('Django', 'Python', 'Cooking', 'Programming',
        'Node JS', 'PHP', 'C', 'C++'
    )

    # for i in range(10):
    #     username = fakegen.first_name()
    #     new_user = User.objects.get_or_create(
    #         username=username,
    #         email=fakegen.email(),
    #         password=fakegen.ean(length=8)
    #
    #     )[0]
    #     new_company = Company.objects.get_or_create(
    #         user=User.objects.get(username=username),
    #         company_name=fakegen.company(),
    #         company_description=fakegen.text(),
    #         company_website=fakegen.url(),
    #         employees_number=fakegen.random_number(digits=2),
    #         company_email=fakegen.company_email(),
    #         country=fakegen.country(),
    #         city=fakegen.city(),
    #         phone_no=fakegen.random_number(digits=10),
    #         address=fakegen.address(),
    #         pincode=fakegen.random_number(digits=6),
    #     )[0]
    #
    #     new_company.save()

    for company in Company.objects.all():

        skills = []
        skills.append(SKILLS[random.randint(0, 7)])
        skills.append(SKILLS[random.randint(0, 7)])
        skills_str = ", ".join(skills)


        new_job = Job.objects.get_or_create(
            company=company,
            job_title=fakegen.job(),
            job_description=fakegen.text(),
            job_type=fakegen.random_element(elements=JOB_TYPE),
            posted_on=fakegen.date_time(),
            expires_on=fakegen.date_time(),
            education_level=fakegen.random_element(elements=EDUCATION_LEVEL),
            vaccancies=fakegen.random_number(digits=2),
            no_of_applicants=fakegen.random_number(digits=2),
            salary=fakegen.random_element(elements=(10000, 15000, 20000, 30000, 50000, 5000, 25000, 2500, 35000)),
            skills=skills_str,
            about_job=fakegen.text(),
            keywords=skills_str,
            experience=fakegen.random_number(digits=1),
            onet_codes=['11-1021.00']

        )[0]

        new_job.save()

if __name__ == '__main__':
    get_data()
    print("DATA ADDED")
