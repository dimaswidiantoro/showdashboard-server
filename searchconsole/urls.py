from django.conf.urls import url
from . import views

app_name = 'searchconsole'

urlpatterns = [
    url(r'^scindonesia/', views.scindonesia, name='scindonesia'),
    url(r'^scphilipines/', views.scphilipines, name='scphilipines'),
    url(r'^scfrance/', views.scfrance, name='scfrance'),
    url(r'^scturkey/', views.scturkey, name='scturkey'),
    url(r'^scindia/', views.scindia, name='scindia'),
    url(r'^scusa/', views.scusa, name='scusa'),
]
