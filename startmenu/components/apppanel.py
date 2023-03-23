from django_unicorn.components import UnicornView
from ..models import AppInfo


class ApppanelView(UnicornView):
    name = ''
    subtitle = ''
    description = ''
    redirect = ''
    src = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        name = kwargs.get('name')
        self.set_name(name)

    def set_name(self, name: str):
        app = AppInfo.objects.get(name=name)
        self.name = app.name
        self.subtitle = app.subtitle
        self.description = app.description
        self.redirect = f'{self.name}:app'
        self.src = f'/image/{app.icon}'
