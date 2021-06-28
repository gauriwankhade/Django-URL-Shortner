from rest_framework import serializers
from .models import *


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ['short_url']


class UniqueKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueKey
        fields = "__all__"
        