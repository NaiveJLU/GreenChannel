import views
from django.conf.urls import url

urlpatterns = [
    url(r'^record$', views.index),
    url(r'^add_user', views.add_user),
    url(r'^update_user', views.update_user),
    url(r'^find_user', views.find_user),
    url(r'^find_alluser', views.find_alluser),
    url(r'^delete_user', views.delete_user),
    url(r'^login', views.login),

    url(r'^add_produce', views.add_produce),
    url(r'^delete_produce', views.delete_produce),
    url(r'^update_produce', views.update_produce),
    url(r'^find_produce', views.find_produce),
    url(r'^find_allproduce', views.find_allproduce),

    url(r'^find_record', views.find_record),
    url(r'^add_record', views.add_record),
    url(r'^update_record', views.update_record),
    url(r'^record_export$', views.record_export),

    url(r'^download', views.download),
]
