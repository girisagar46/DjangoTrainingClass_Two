from django.conf.urls import url
from django.views.generic import TemplateView

from blog import views

app_name = 'blog'

urlpatterns = [
    #url(r'^$', views.home, name="home"),
    #url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^$', views.PostListView.as_view(), name="home"),
    url(r'post_detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail'),
    # url(r'^about/', views.about, name="about"),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name="about"),
    #url(r'^contact/', views.contact, name="contact"),
    url(r'^contact/', views.ContactView.as_view(), name="contact"),
]