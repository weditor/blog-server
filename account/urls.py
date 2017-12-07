from django.conf.urls import url, include
from .views import GetUser, login_view, logout_view

urlpatterns = [
    url(r'^profile/$', GetUser),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view),
]


