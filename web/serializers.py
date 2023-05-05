from rest_framework import serializers

from . import models as m


class BirthdatCelebrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.BirthdayCelebrant
        fields = "__all__"


class SpotLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.SpotLight
        fields = "__all__"
