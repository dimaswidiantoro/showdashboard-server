from django.conf.urls import url
from . import views

app_name = 'searchconsole'

urlpatterns = [
    url(r'^scindonesia/', views.scindonesia, name='scindonesia'),
    url(r'^scphilipines/', views.scphilipines, name='scphilipines'),
    url(r'^scfrance/', views.scfrance, name='scfrance'),
]
