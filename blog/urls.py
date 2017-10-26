
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'article', ArticleViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]


