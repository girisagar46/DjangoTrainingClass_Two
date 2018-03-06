from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostListApiView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)$', views.PostApiView.as_view(), name='post_rud'),
]