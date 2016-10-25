import views
from django.conf.urls import url

urlpatterns = [
    url(r'^record', views.index),
]
