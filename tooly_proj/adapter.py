from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from applicant.models import Applicant

class GetURLAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = ""
        if (Applicant.objects.filter(user=request.user).exists()):
            # If user = Applicant, redirect him to applicant's homepage after login
            path = "/"
        else:
            # else, redirect him to recruiter's homepage after login
            path = "/recruiter/recruiter_home"
        return path
