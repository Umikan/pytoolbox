from django.urls import path
from . import views

app_name = 'transcribe'

urlpatterns = [
    path('', views.transcriber, name='app'),
    path('clip/', views.transcribe_clip),
]
