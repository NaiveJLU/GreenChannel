import views
from django.conf.urls import url

urlpatterns = [
    url(r'^record', views.index),
    url(r'^add_user', views.add_user),
    url(r'^login', views.login),
]
