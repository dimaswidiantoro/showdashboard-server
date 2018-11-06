from django.conf.urls import url
from . import views

app_name = 'android'

urlpatterns = [
    url(r'^android/', views.android, name='android'),
    url(r'^USandroid/', views.USandroid, name='USandroid'),
]
