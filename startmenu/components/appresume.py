from django_unicorn.components import UnicornView
from django.utils.functional import cached_property
from ..models import AppInfo


class AppresumeView(UnicornView):
