
from django.conf.urls import url, include
from django.contrib import admin

from crypto.views import get_crypto

urlpatterns = [
    url(r'', include("blog.urls")),
    url(r'^crypto/', include("crypto.urls")),
    url(r'^admin/', admin.site.urls),
]
