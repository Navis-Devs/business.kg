from rest_framework import serializers
from .models import AutoUP, Urgent, Highlight


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