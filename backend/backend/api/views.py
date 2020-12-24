from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import CarSerializer
from cars.models import Car


class CarList(APIView):
    """
    Read-only API endpoint for a list of all Car objects.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Car.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer_context = {
            'request': request,
        }
        serializer = CarSerializer(queryset, context=serializer_context, many=True)
        return Response(serializer.data)


class CarDetail(APIView):
    """
    Read-only API endpoint for a single Car object.
    """
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        car = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = CarSerializer(car, context=serializer_context)
        return Response(serializer.data)
