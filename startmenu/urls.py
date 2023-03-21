from django.urls import path
from .components.apppanel import ApppanelView
from . import views

app_name = 'startmenu' 

urlpatterns = [
    path('', views.startmenu),
    path("apps/<int:pk>/", ApppanelView.as_view(), name="apps")
]
