from rest_framework import serializers
from .models import AutoUP


class AutoUPSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoUP
        fields = "__all__"
