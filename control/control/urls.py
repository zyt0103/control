from django.conf.urls import include, url
from django.contrib import admin

from . import views

from django.views.generic import View

urlpatterns = [
    # Examples:
    # url(r'^$', 'control.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Index.as_view()),
    url(r'^modu/', include('control.apps.modu')),
    url(r'^demo/', include('control.apps.demo')),
]
