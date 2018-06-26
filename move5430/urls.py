"""move5430 URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Main App Views
    url(r'^$', main_views.index, name='index'),
    url(r'^about/$', main_views.about, name='about'),
    url(r'^contact/$', main_views.contact, name='contact'),
    url(r'^plans/$', main_views.plans, name='plans'),
    url(r'^cody/$', main_views.cody, name='cody'),
    url(r'^aboutcody/$', main_views.aboutcody, name='about_cody'),
    url(r'^codynow/$', main_views.codynow, name='cody_now'),
    url(r'^cara/$', main_views.cara, name='cara'),
    url(r'^aboutcara/$', main_views.aboutcara, name='about_cara'),
    url(r'^caranow/$', main_views.caranow, name='cara_now'),
    url(r'^letters/$', main_views.letters, name='letters'),
    url(r'^thx/$', main_views.thanks, name='thanks'),

]

if settings.DEBUG:	
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)