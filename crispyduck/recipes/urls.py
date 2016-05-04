from django.conf.urls import include, url
from .views import main_view, index_view, details_view, review_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', main_view, name='main'),
    url(r'^recipes/$', index_view, name='index'),
    url(r'^(?P<id>\d+)$', details_view, name='details'),
    url(r'^(?P<id>\d+)/review$', review_view, name='review'),
]
