from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from api.models import Test
from api.serializers import TestSerializer, ContentSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def test_list(request):
    tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def test_detail(request, pk):
    test = Test.objects.get(pk=pk)
    serializer = ContentSerializer(test)
    return Response(serializer.data)
