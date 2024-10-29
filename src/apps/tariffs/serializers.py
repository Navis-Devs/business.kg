from rest_framework import serializers
from .models import Top, AutoUP, Urgent, Highlight


class TopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top
        fields = "__all__"


class AutoUPSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoUP
        fields = "__all__"


class UrgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urgent
        fields = "__all__"


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = "__all__"


class SubscribeToTariffSerializer(serializers.Serializer):
    # Model
    obj_table = serializers.CharField(required=True)
    # Object id
    obj_id = serializers.CharField(required=True)
    # tariff model
    tariff_table = serializers.CharField(required=True)
    # Tariff id
    tariff_id = serializers.UUIDField(required=True)

    class Meta:
        fields = "__all__"
