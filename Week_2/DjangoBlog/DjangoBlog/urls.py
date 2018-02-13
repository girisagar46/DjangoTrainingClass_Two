
from django.conf.urls import url
from django.contrib import admin

from blog.views import home, about, contact

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^about/', about, name="about"),
    url(r'^contact/', contact, name="contact"),
    url(r'^admin/', admin.site.urls),
]
