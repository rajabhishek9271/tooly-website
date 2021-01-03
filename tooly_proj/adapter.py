from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from applicant.models import Applicant

class GetURLAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = ""
        if (Applicant.objects.filter(user=request.user).exists()):
            path = "/"
        else:
            path = "/recruiter/recruiter_home"
        return path
