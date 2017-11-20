from django.conf.urls import url, include
from .views import GetUser

urlpatterns = [
    url(r'^profile/$', GetUser),
]


