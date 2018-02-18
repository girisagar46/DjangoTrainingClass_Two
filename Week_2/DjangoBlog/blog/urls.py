from django.conf.urls import url

from blog.views import home, about, contact, get_one_post

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'post/(?P<pk>\d+)', get_one_post, name='detail'),
    url(r'^about/', about, name="about"),
    url(r'^contact/', contact, name="contact"),
]