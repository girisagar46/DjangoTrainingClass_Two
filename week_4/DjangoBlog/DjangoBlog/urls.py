
from django.conf.urls import url, include
from django.contrib import admin

from crypto.views import get_crypto

admin.site.site_header = "Django Blog Admin"
admin.site.site_title = 'Blog Admin Panel'
admin.site.index_title = 'Dblog Admininstration'

urlpatterns = [
    url(r'', include("blog.urls")),
    url(r'^crypto/', include("crypto.urls")),
    url(r'^admin/', admin.site.urls),
]
