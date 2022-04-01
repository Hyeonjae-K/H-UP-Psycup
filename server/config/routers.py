from rest_framework import routers

from api.viewsets import TestViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register(r'tests', TestViewSet, 'tests')
router.register(r'contents', ContentViewSet, 'contents')
