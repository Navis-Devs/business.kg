from rest_framework import serializers
from apps.tariffs import models

class PlansSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Plans
        fields = '__all__'
        
class TariffSerializers(serializers.ModelSerializer):
    plans = PlansSerializers(many=True)
    class Meta:
        model = models.Tariff
        fields = ['id', 'name', 'amount', 'img', 'description', 'period', 'plans']


class ApplyTariffSerializer(serializers.Serializer):
    property_id = serializers.IntegerField()
    tariff_id = serializers.IntegerField()
    plan_id = serializers.IntegerField()
    color = serializers.CharField(required=False)
    up_time = serializers.TimeField(required=False)

    def validate(self, data):
        try:
            data['property_instance'] = models.Property.objects.get(id=data['property_id'])
        except models.Property.DoesNotExist:
            raise serializers.ValidationError("Объект с указанным ID не найден.")
        
        try:
            data['tariff_instance'] = models.Tariff.objects.get(id=data['tariff_id'])
        except models.Tariff.DoesNotExist:
            raise serializers.ValidationError("Тариф с указанным ID не найден.")
        
        tariff_instance = data['tariff_instance']
        try:
            data['plan_instance'] = tariff_instance.plans.get(id=data['plan_id'])
        except models.Plans.DoesNotExist:
            raise serializers.ValidationError(f"План с ID {data['plan_id']} не найден для выбранного тарифа.")
        
        return data


    def apply_tariff(self):
        # Применение тарифа к объекту Property
        property_instance = self.validated_data['property_instance']
        tariff_instance = self.validated_data['tariff_instance']
        plan_instance = self.validated_data['plan_instance']
        color_instance = self.validated_data.get('color', None)
        up_time_instance = self.validated_data.get('up_time', None)
        print("DATA COLORS AND TIME " * 10,color_instance, up_time_instance)
        property_instance.product_id = tariff_instance
        property_instance.plans = plan_instance
        property_instance.ad_color = color_instance
        property_instance.autoup_time =  up_time_instance
        property_instance._apply_tariff()  
        property_instance.save()
        return property_instance