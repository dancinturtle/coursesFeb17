from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^courses$', views.add),
    url(r'^renderDelete/(?P<id>\d+)$', views.renderDelete),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
