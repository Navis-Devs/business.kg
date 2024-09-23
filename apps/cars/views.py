from rest_framework import generics
from rest_framework.response import Response

from django.db.models import Min, Max

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

import base64
import hashlib
import datetime

data = {
    # 'car_types': CarTypeSerializer(CarType.objects.all(), many=True).data,
    # 'car_marks': CarMarkSerializer(CarMark.objects.all(), many=True).data,
    # 'car_models': CarModelSerializer(CarModel.objects.all(), many=True).data,
    # 'car_generations': CarGenerationSerializer(CarGeneration.objects.all(), many=True).data,
    # 'car_series': CarSerieSerializer(CarSerie.objects.all(), many=True).data,
    # 'car_modifications': CarModificationSerializer(CarModification.objects.all(), many=True).data,
    # 'car_characteristics': CarCharacteristicSerializer(CarCharacteristic.objects.all(), many=True).data,
    # 'car_characteristic_values': CarCharacteristicValueSerializer(CarCharacteristicValue.objects.all(), many=True).data,
    # 'car_equipments': CarEquipmentSerializer(CarEquipment.objects.all(), many=True).data,
    # 'car_options': CarOptionSerializer(CarOption.objects.all(), many=True).data,
    # 'car_option_values': CarOptionValueSerializer(CarOptionValue.objects.all(), many=True).data,
}


# data_str = str(data).encode('utf-8')
# hashed_data = hashlib.sha256(data_str).hexdigest()
# encoded_data = base64.b64encode(data_str).decode('utf-8')


class CarDataListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        id_car_mark = request.query_params.get("mark")
        id_car_model = request.query_params.get("model")
        year = request.query_params.get("year")

        ''' filter with mark '''
        if id_car_mark:
            response = {
                "🥰": "🥵",
                "type": "models",
                "data": CarModelSerializer(
                CarModel.objects.filter(
                    id_car_mark__id=id_car_mark
                ), many=True).data}

            ''' filter with year (filtering with function)'''
            if id_car_model:
                response = {
                    "🥰": "🥵",
                    "type": "years",
                    "data": self.get_year(id_car_model)}

                ''' filter with year '''
                if year:
                    response = {
                        "🥰": "🥵",
                        "type": "series",
                        "data": CarGenerationSerializer(
                        CarGeneration.objects.filter(
                            id_car_model__id=id_car_model,
                            year_end__gte=year,
                            year_begin__lte=year
                        ).order_by("year_begin"), many=True).data}

        else:
            response = {
                "🥰": "🥵",
                "type": "marks",
                "data": CarMarkSerializer(
                CarMark.objects.all(), many=True).data}

        return Response(response)

    def get_year(self, id_car_model):
        car_generations = CarGeneration.objects.filter(id_car_model__id=id_car_model).aggregate(
            min_year=Min("year_begin"),
            max_year=Max("year_end")
        )
        min_year = car_generations.get("min_year")
        max_year = car_generations.get("max_year")

        if max_year == "NULL":
            max_year = datetime.date.today().year

        if min_year is not None and max_year is not None:
            return [year for year in range(int(min_year), int(max_year) + 1)]
        else:
            return []
