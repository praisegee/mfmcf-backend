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
        )
        serializer = s.BirthdatCelebrantSerializer(celebrants, many=True)
        return response.Response(serializer.data, status=200)


class SpotLightAPI(viewsets.ModelViewSet):
    queryset = m.SpotLight.objects.all()
    serializer_class = s.SpotLightSerializer
