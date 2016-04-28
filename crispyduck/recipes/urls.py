from django.conf.urls import include, url
from .views import main_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', main_view, name='main'),
]