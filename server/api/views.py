from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from api.models import Test
from api.serializers import TestListSerializer, TestDetailSerializer, TestResultSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def test_list(request):
    tests = Test.objects.all()
    serializer = TestListSerializer(tests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def test_detail(request, pk):
    test = Test.objects.get(pk=pk)
    serializer = TestDetailSerializer(test)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def test_result(request, pk):
    result = Test.objects.get(pk=pk)
    serializer = TestResultSerializer(result)
    return Response(serializer.data)
