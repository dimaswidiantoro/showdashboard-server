from django.conf.urls import url
from . import views

app_name = 'analytics'

urlpatterns = [
    url(r'^analytics/', views.analytics, name='analytics'),
    url(r'^httpoolData/', views.httpoolData, name='httpoolData'),
]
