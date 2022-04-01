from rest_framework import viewsets

from api.models import Test
from api.serializers import TestSerializer, TestListSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestListViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestListSerializer
