from rest_framework import serializers
from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue, CarColors
)
from apps.cars_posts.models import (
    CarMark,
    CarModel,
    CarType,
    Currency,
    Region,
    Exchange,
    Towns,
    RegistrationCountry,
    CommentAllowed,
    Transmission, 
    Fuel,
    GearBox,
    SteeringWheel,
    Exterior,
    Interior,
    Media,
    Safety,
    OtherOptions,
    Condition,
    FeaturedOption,
    GeneralOptions,
)


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ['id', 'name']


class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = ['id', 'name', 'img']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'is_popular']


class CarGenerationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarGeneration
        fields = ['id', 'name', 'img', 'year_begin', 'year_end']


class CarSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSerie
        fields = ['id', 'name']


class CarModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModification
        fields = ['id', 'name']

class CarCharacteristicValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='id_car_characteristic.name')

    class Meta:
        model = CarCharacteristicValue
        fields = ['name', 'value', 'unit']


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
###

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['id', 'name']

class RegistrationCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCountry
        fields = ['id', 'name']
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarColors
        fields = ['id', 'name', 'color']

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ['id', 'name']

class GearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearBox
        fields = ['id', 'name']

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['id', 'name']

class CommentAllowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentAllowed
        fields = ['id', 'name']

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOptions
        fields = ['id', 'name']

class SteeringWheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteeringWheel
        fields = ['id', 'name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'sign', 'is_default']

class ExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = ['id', 'name']   

class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = ['id', 'name']

class TownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Towns
        fields = ['id', 'name'] 

class RegionSerializer(serializers.ModelSerializer):
    towns = TownsSerializer(many=True)
    class Meta:
        model = Region
        fields = ['id', 'name', 'towns']         

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'name']  

class OtherOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherOptions
        fields = ['id', 'name']    

class FeaturedOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedOption
        fields = ['id', 'name'] 

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['id', 'name'] 

class CombinedSerializer(serializers.Serializer):
    car_type = CarTypeSerializer(many=True)
    car_condition = ConditionSerializer(many=True)
    color = ColorSerializer(many=True)
    currency = CurrencySerializer(many=True)
    comment_allowed = CommentAllowedSerializer(many=True)
    registration_country = RegistrationCountrySerializer(many=True)
    configuration = ConfigurationSerializer(many=True)
    exterior = ExteriorSerializer(many=True)
    interior = InteriorSerializer(many=True)
    media = MediaSerializer(many=True)
    other_option = OtherOptionsSerializer(many=True)
    gear_box = GearBoxSerializer(many=True)
    fuel = FuelSerializer(many=True)
    featured_option = FeaturedOptionSerializer(many=True)
    transmission = TransmissionSerializer(many=True)
    exchange = ExchangeSerializer(many=True)
    steering_wheel = SteeringWheelSerializer(many=True)
    region = RegionSerializer(many=True)