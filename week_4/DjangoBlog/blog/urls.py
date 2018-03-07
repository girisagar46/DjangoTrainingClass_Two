from django.conf.urls import url, include
from django.views.generic import TemplateView

from blog import views

app_name = 'blog'

urlpatterns = [
    #url(r'^$', views.home, name="home"),
    #url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^$', views.PostListView.as_view(), name="home"),
    url(r'^post_detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail'),
    url(r'^new/', views.new_post, name='new_post'),
    url(r'^register/',views.resister, name='register'),
    # url(r'^about/', views.about, name="about"),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name="about"),
    #url(r'^contact/', views.contact, name="contact"),
    #url(r'^contact/', views.ContactView.as_view(), name="contact"),
    url(r'^contact/', views.contact_us, name="contact"),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),
    url(r'^search/', views.search, name='search'),
    url(r'^apis/', views.api_doc, name='api_doc'),
    url(r'^api/posts/', views.post_list_api, name='list_api_view'),
    url(r'^api/post/(?P<pk>[0-9]+)/$', views.post_detail_api, name='detail_api_view'),
    url('^apii/', include('blog.api.urls', namespace='blogapi'))
]