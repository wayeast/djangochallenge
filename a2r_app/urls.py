from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.a2r_convert, name='a2r_convert'),
]
