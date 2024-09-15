from rest_framework import generics
from rest_framework.response import Response
from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue
)
from .serializers import (
    CarTypeSerializer, CarMarkSerializer, CarModelSerializer, CarGenerationSerializer,
    CarSerieSerializer, CarModificationSerializer, CarCharacteristicSerializer,
    CarCharacteristicValueSerializer, CarEquipmentSerializer, CarOptionSerializer,
    CarOptionValueSerializer
)

class CarDataListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            'car_types': CarTypeSerializer(CarType.objects.all(), many=True).data,
            'car_marks': CarMarkSerializer(CarMark.objects.all(), many=True).data,
            'car_models': CarModelSerializer(CarModel.objects.all(), many=True).data,
            'car_generations': CarGenerationSerializer(CarGeneration.objects.all(), many=True).data,
            'car_series': CarSerieSerializer(CarSerie.objects.all(), many=True).data,
            'car_modifications': CarModificationSerializer(CarModification.objects.all(), many=True).data,
            'car_characteristics': CarCharacteristicSerializer(CarCharacteristic.objects.all(), many=True).data,
            'car_characteristic_values': CarCharacteristicValueSerializer(CarCharacteristicValue.objects.all(), many=True).data,
            'car_equipments': CarEquipmentSerializer(CarEquipment.objects.all(), many=True).data,
            'car_options': CarOptionSerializer(CarOption.objects.all(), many=True).data,
            'car_option_values': CarOptionValueSerializer(CarOptionValue.objects.all(), many=True).data,
        }
        return Response(data)
