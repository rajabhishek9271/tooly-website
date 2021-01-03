from .models import Company
from django.core.exceptions import PermissionDenied

class MustBeCompanyMixin:

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if Company.objects.filter(user=user).exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
