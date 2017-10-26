
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleViewset, TagViewset, ReplyViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'article', ArticleViewset)
router.register(r'tag', TagViewset)
router.register(r'reply', ReplyViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]


