"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import frontpage.views
import homepage.views
import accounts.views
import searchconsole.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', frontpage.views.frontpage, name="frontpage"),
    url(r'^stakeholder', frontpage.views.stakeholder, name="stakeholder"),
    url(r'^$', homepage.views.homepage, name="homepage"),
    url(r'^homepage2', homepage.views.homepage2, name="homepage2"),
    url(r'^halamandepan', homepage.views.halamandepan, name="halamandepan"),
    url(r'^brainlyhttpool', homepage.views.brainlyhttpool, name="brainlyhttpool"),
    url(r'^internalteam', homepage.views.internalteam, name="internalteam"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^searchconsole/', include('searchconsole.urls')),

]
