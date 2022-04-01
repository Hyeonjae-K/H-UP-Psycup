from rest_framework import routers

from api.viewsets import TestViewSet, TestListViewSet

router = routers.DefaultRouter()
router.register(r'tests', TestListViewSet, 'tests')
router.register(r'contents', TestViewSet, 'contents')
