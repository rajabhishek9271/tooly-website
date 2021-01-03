from .models import Applicant
from django.core.exceptions import PermissionDenied

class MustBeApplicantMixin:

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if Applicant.objects.filter(user=user).exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
