from rest_framework import serializers
from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue
)


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ['id', 'name']


class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = ['id', 'name', 'name_rus', 'id_car_type']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'name_rus', 'id_car_mark', 'id_car_type']


class CarGenerationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarGeneration
        fields = ['id', 'name', 'year_begin', 'year_end', 'id_car_model', 'id_car_type']


class CarSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSerie
        fields = ['id', 'name', 'id_car_model', 'id_car_generation', 'id_car_type']

# до этого все сделал

class CarModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModification
        fields = ['id', 'name', 'id_car_serie', 'id_car_model', 'id_car_type']


class CarCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCharacteristic
        fields = ['id', 'name', 'id_parent', 'id_car_type']


class CarCharacteristicValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCharacteristicValue
        fields = ['id', 'value', 'unit', 'id_car_characteristic', 'id_car_modification', 'id_car_type']


class CarEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEquipment
        fields = ['id', 'name', 'id_car_modification', 'price_min', 'id_car_type', 'year']


class CarOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOption
        fields = ['id', 'name', 'id_parent', 'id_car_type']


class CarOptionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOptionValue
        fields = ['id', 'is_base', 'id_car_option', 'id_car_equipment', 'id_car_type']
