from django.contrib import admin
from .models import Applicant, Application

# Register your models here.
admin.site.register(Application)
admin.site.register(Applicant)
