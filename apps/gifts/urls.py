from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.home, name = 'login_home'),
    url(r'^create$', views.create, name = 'wishlist_create'),
    url(r'^createwish$', views.createwish, name = 'wishlist_createwish'),
    url(r'^join$', views.join, name = 'wishlist_join'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = 'wishlist_remove'),
    url(r'^unwish/(?P<id>\d+)$', views.unwish, name = 'wishlist_unwish'),
    url(r'^show/(?P<id>\d+)$', views.show, name='wishlist_show')
]
