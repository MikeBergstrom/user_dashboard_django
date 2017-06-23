from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^setadmin$', views.setadmin),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^edit/update$', views.update),
    url(r'^edit/password$', views.password),
    url(r'^edit/description$', views.description),
    url(r'^adduser$', views.adduser),
    url(r'^newuser$', views.newuser),
    url(r'^remove/(?P<id>\d+)$', views.confirm),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^show/message$', views.message),
    url(r'^show/comment$', views.comment),
    url(r'^logout$', views.logout)

]