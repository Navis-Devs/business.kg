from rest_framework import generics
from rest_framework.response import Response

from django.db.models import Min, Max, Q

from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue
)
from .serializers import (
    CarTypeSerializer, CarMarkSerializer, CarModelSerializer, CarGenerationSerializer,
    CarSerieSerializer, CarModificationSerializer,
    CarCharacteristicValueSerializer, CarEquipmentSerializer, CarOptionSerializer,
    CarOptionValueSerializer
)

from apps.helpers.choices import Currency, FuelType, DriveType, TransmissionType, SteeringWheelPosition, CarCondition, \
    MileageUnit, AvailabilityStatus, RegistrationCountry, VehicleStatus, ExchangePossibility

import base64
import hashlib
import datetime
import json

# data_str = str(data).encode('utf-8')
# hashed_data = hashlib.sha256(data_str).hexdigest()
# encoded_data = base64.b64encode(data_str).decode('utf-8')


class CarDataListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        id_car_mark = request.query_params.get("mark")
        id_car_model = request.query_params.get("model")
        year = request.query_params.get("year")
        id_car_generation = request.query_params.get("generation")
        id_car_serie = request.query_params.get("serie")
        car_fuel = request.query_params.get("fuel")
        transmission = request.query_params.get("transmission")
        gear_box = request.query_params.get("gear_box")

        ''' filter with mark | output = marks'''
        if id_car_mark:
            response = {
                "type": "models",
                "data": CarModelSerializer(
                CarModel.objects.filter(
                    id_car_mark__id=id_car_mark
                ), many=True).data}

            ''' filter with year (filtering with function) | output = available years'''
            if id_car_model:
                response = {
                    "type": "years",
                    "data": self.get_year(id_car_model)}

                ''' filter with year | output = generations'''
                if year:
                    response = {
                        "type": "series",
                        "data": CarSerieSerializer(
                        CarSerie.objects.filter(
                            id_car_model__id=id_car_model,
                            id_car_generation__year_end__gte=year,
                            id_car_generation__year_begin__lte=year
                        ),
                        # ).distinct('name'),
                            many=True).data}

                    ''' filter with serie | output = generation '''
                    if id_car_serie:
                        response = {
                            "type": "generations",
                            "data": CarGenerationSerializer(
                                CarGeneration.objects.filter(
                                    id_car_model__id=id_car_model,
                                    year_end__gte=year,
                                    year_begin__lte=year,
                                    car_serie__id=id_car_serie
                                ).order_by("year_begin"), many=True).data}

                        ''' filter with generation | output = fuel type '''
                        if id_car_generation:
                            response = {
                                "type": "fuels",
                                "data":
                                    list(
                                        set(
                                            CarCharacteristicValue.objects.filter(
                                                id_car_characteristic__name="Тип двигателя",
                                                id_car_modification__id_car_serie__id=id_car_serie
                                            ).values_list("value", flat=True)
                                        )
                                    )
                            }

                            ''' filter with car_fuel | output = transmission '''
                            if car_fuel:
                                response = {
                                    "type": "transmissions",
                                    "data":
                                        list(
                                            set(
                                                CarCharacteristicValue.objects.filter(
                                                    id_car_characteristic__name="Привод",
                                                    id_car_modification__id_car_serie_id=id_car_serie
                                                ).values_list("value", flat=True)
                                            )
                                        )
                                }

                                ''' filter with transmission | output = gear_box '''
                                if transmission:
                                    response = {
                                        "type": "gear_boxes",
                                        "data":
                                            list(
                                                set(
                                                    CarCharacteristicValue.objects.filter(
                                                        id_car_characteristic__name="Тип КПП",
                                                        id_car_modification__id_car_serie_id=id_car_serie
                                                    ).values_list("value", flat=True)
                                                )
                                            )
                                    }

                                    ''' filter with gear_box '''
                                    if gear_box:
                                        response = {
                                            "type": "engine",
                                            "data": list(
                                                        set(
                                                            CarCharacteristicValue.objects.filter(
                                                                id_car_characteristic__name="Объем двигателя",
                                                                id_car_modification__id_car_serie_id=id_car_serie,
                                                            ).values_list("value", flat=True)
                                                        )
                                                    )
                                        }


                    # "data": CarModificationSerializer(
                    #     CarModification.objects.filter(
                    #         id_car_model=id_car_model,
                    #         id_car_serie=id_car_serie
                    #     ), many=True).data}


                    # ''' filter with generation | output = series '''
                    # if id_car_generation:
                    #     response = {
                    #         "type": "serie",
                    #         "data": CarSerieSerializer(
                    #         CarSerie.objects.filter(
                    #             id_car_model=id_car_model,
                    #             id_car_generation=id_car_generation,
                    #         ), many=True).data}

                    #     ''' filter with serie | output = modification '''
                    #     if id_car_serie:
                    #         response = {
                    #             "type": "modification",
                    #             "data": CarModificationSerializer(
                    #                 CarModification.objects.filter(
                    #                     id_car_model=id_car_model,
                    #                     id_car_serie=id_car_serie
                    #                 ), many=True).data}
                    #
                    #         ''' filter with modification | output = characteristic '''
                    #         if id_car_modification:
                    #             response = {
                    #                 "type": "characteristic",
                    #                 "data": CarCharacteristicValueSerializer(
                    #                     CarCharacteristicValue.objects.filter(
                    #                         id_car_modification__id=id_car_modification
                    #                     ), many=True).data,
                    #                 "fuel_type": self.get_fuel_type()}


        else:
            ''' output = all marks'''
            response = {
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


    def get_fuel_type(self,):
        from apps.cars.models import CarCharacteristicValue
        fuel = list(
            set(
                CarCharacteristicValue.objects.filter(
                    id_car_characteristic__name="Тип двигателя"
                ).values_list("value", flat=True)))
        return fuel


class ChoicesView(generics.GenericAPIView):
    def get(self, request, language):
        if language not in ["KY", "RU", "EN"]:
            return Response({"response": False, "message": "No language found"})

        file_path = f"apps/helpers/languages/{language}_car_data.json"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return Response(data)
        except FileNotFoundError:
            return Response({"response": False, "message": "File not found"}, status=404)