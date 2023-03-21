from django.http import HttpResponse
from django.template import loader
from .models import AppInfo


def startmenu(request):
    apps = AppInfo.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'apps': apps,
    }
    return HttpResponse(template.render(context, request))
