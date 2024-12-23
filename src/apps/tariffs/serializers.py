from rest_framework import serializers
from apps.tariffs import models
from apps.house import models as house_models
from apps.cars_posts import models as car_models

class PlansSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Plans
        fields = '__all__'
        

class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = '__all__'
        
class TariffSerializers(serializers.ModelSerializer):
    colors = ColorSerializers(many=True, read_only=True)
    plans = PlansSerializers(many=True)
    class Meta:
        model = models.Tariff
        fields = ['id', 'name', 'amount', 'img', 'description', 'period', 'colors', 'plans']


class ApplyTariffSerializer(serializers.Serializer):
    object_type = serializers.ChoiceField(choices=[('car', 'car'), ('house', 'house')])
    object_id = serializers.UUIDField(format='hex')
    tariff_id = serializers.IntegerField()
    plan_id = serializers.IntegerField()
    color = serializers.CharField(required=False)
    up_time = serializers.TimeField(required=False)

    def validate(self, data):
        object_type = data['object_type']
        object_id = data['object_id']
        if object_type == 'house':
            try:
                data['object_instance'] = house_models.Property.objects.get(id=object_id)
            except house_models.Property.DoesNotExist:
                raise serializers.ValidationError("Объект недвижимости с указанным ID не найден.")
        elif object_type == 'car':
            try:
                data['object_instance'] = car_models.CarsPosts.objects.get(id=object_id)
            except car_models.CarsPosts.DoesNotExist:
                raise serializers.ValidationError("Объект автомобиля с указанным ID не найден.")
        else:
            raise serializers.ValidationError("Неверный тип объекта.")
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
        object_instance = self.validated_data['object_instance']
        tariff_instance = self.validated_data['tariff_instance']
        plan_instance = self.validated_data['plan_instance']
        color_instance = self.validated_data.get('color', None)
        up_time_instance = self.validated_data.get('up_time', None)

        object_instance.product_id = tariff_instance
        object_instance.plans = plan_instance
        object_instance.ad_color = color_instance
        object_instance.autoup_time = up_time_instance
        object_instance._apply_tariff()  
        object_instance.save()

        return object_instance