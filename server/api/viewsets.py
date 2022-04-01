from rest_framework import viewsets

from api.models import Test
from api.serializers import TestSerializer, ContentSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = ContentSerializer
