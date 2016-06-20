from django.conf.urls import include, url

from . import views as demod_view

urlpatterns = [
    url(r'demodsignal$', demod_view.DemodSignal.as_view()),
    url(r'demodtypecreate$', demod_view.DemodTypeCreate.as_view())
    # url(r'describe$', modu_view.DescribeSignal.as_view()),
    # url(r'delete$', modu_view.DeleteSignal.as_view()),
    # url(r'get$', modu_view.GetSignal.as_view()),


]