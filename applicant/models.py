from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from recruiter.models import Job
# Create your models here.


class Applicant(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='applicants/profile_pics')
    resume = models.FileField(upload_to='applicants/resumes', max_length=300)
    country = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    address = models.CharField(max_length=500)
    pincode = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    applied_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.applicant.user.first_name} -> {self.applied_job.job_title}"

    def save(self, *args, **kwargs):

        required_job = Job.objects.get(id=self.applied_job.id)
        if(self.is_accepted):
            required_job.vaccancies -= 1
            required_job.save()

            super().save(*args, **kwargs)  # Call the "real" save() method.
            return None
        required_job.no_of_applicants += 1
        required_job.save()
        super().save(*args, **kwargs)  # Call the "real" save() method.
