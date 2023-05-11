from django.utils import timezone
from rest_framework import decorators, viewsets, response, generics

from . import models as m
from . import serializers as s


class BirthdatCelebrantAPI(viewsets.ModelViewSet):
    queryset = m.BirthdayCelebrant.objects.all()
    serializer_class = s.BirthdatCelebrantSerializer

    @decorators.action(methods=["GET"], detail=False, url_path="current-month")
    def get_this_month_celebrants(self, request, *args, **kwargs):
        current_month = timezone.now().month
        celebrants = m.BirthdayCelebrant.objects.filter(
            birthday__endswith=str(current_month)
        ).order_by("birthday")
        serializer = s.BirthdatCelebrantSerializer(celebrants, many=True)
        return response.Response(serializer.data, status=200)


class SpotLightAPI(viewsets.ModelViewSet):
    queryset = m.SpotLight.objects.all()
    serializer_class = s.SpotLightSerializer


class ExecutiveAPI(viewsets.ModelViewSet):
    queryset = m.Executive.objects.all()
    serializer_class = s.ExecutiveSerializer

    @decorators.action(methods=["GET"], detail=False, url_path="oye")
    def oye_excos(self, request, *args, **kwargs):
        executives = m.Executive.objects.filter(campus="Oye")
        serializer = s.ExecutiveSerializer(executives, many=True)
        return response.Response(serializer.data, status=200)

    @decorators.action(methods=["GET"], detail=False, url_path="ikole")
    def ikole_excos(self, request, *args, **kwargs):
        executives = m.Executive.objects.filter(campus="Ikole")
        serializer = s.ExecutiveSerializer(executives, many=True)
        return response.Response(serializer.data, status=200)
