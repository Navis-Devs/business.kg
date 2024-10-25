from rest_framework import serializers
from .models import AutoUP, Urgent


class AutoUPSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoUP
        fields = "__all__"


class UrgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urgent
        fields = "__all__"