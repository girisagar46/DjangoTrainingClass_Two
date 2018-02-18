
from django.conf.urls import url


from crypto.views import get_crypto

urlpatterns = [
    url(r'^coin/', get_crypto, name="crypto"),
]