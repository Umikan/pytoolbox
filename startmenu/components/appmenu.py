from django_unicorn.components import UnicornView
from django.utils.functional import cached_property
from ..models import AppInfo


class AppmenuView(UnicornView):
    app_name = None

    @cached_property
    def apps(self):
        return AppInfo.objects.all().values()
