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
    CarSerieSerializer, CarModificationSerializer,
    CarCharacteristicValueSerializer, CarEquipmentSerializer, CarOptionSerializer,
    CarOptionValueSerializer
)

from apps.helpers.choices import Currency, FuelType, DriveType, TransmissionType, SteeringWheelPosition, CarCondition, \
    MileageUnit, AvailabilityStatus, RegistrationCountry, VehicleStatus, ExchangePossibility

import base64
import hashlib
import datetime

# data_str = str(data).encode('utf-8')
# hashed_data = hashlib.sha256(data_str).hexdigest()
# encoded_data = base64.b64encode(data_str).decode('utf-8')


class CarDataListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        id_car_mark = request.query_params.get("mark")
        id_car_model = request.query_params.get("model")
        year = request.query_params.get("year")
        id_car_generation = request.query_params.get("gen")
        id_car_serie = request.query_params.get("serie")
        id_car_modification = request.query_params.get("mod")

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
                        "type": "generations",
                        "data": CarGenerationSerializer(
                        CarGeneration.objects.filter(
                            id_car_model__id=id_car_model,
                            year_end__gte=year,
                            year_begin__lte=year
                        ).order_by("year_begin"), many=True).data}

                    ''' filter with generation | output = series '''
                    if id_car_generation:
                        response = {
                            "type": "serie",
                            "data": CarSerieSerializer(
                            CarSerie.objects.filter(
                                id_car_model=id_car_model,
                                id_car_generation=id_car_generation,
                            ), many=True).data}

                        ''' filter with serie | output = modification '''
                        if id_car_serie:
                            response = {
                                "type": "modification",
                                "data": CarModificationSerializer(
                                    CarModification.objects.filter(
                                        id_car_model=id_car_model,
                                        id_car_serie=id_car_serie
                                    ), many=True).data}

                            ''' filter with modification | output = characteristic '''
                            if id_car_modification:
                                response = {
                                    "type": "characteristic",
                                    "data": CarCharacteristicValueSerializer(
                                        CarCharacteristicValue.objects.filter(
                                            id_car_modification__id=id_car_modification
                                        ), many=True).data,
                                    "fuel_type": self.get_fuel_type()}


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
    def get(self, request):
        data = {
            "data": [
                {
                    "label": "Currency",
                    "key": [
                        {"key": Currency.USD, "value": Currency.USD.label},
                        {"key": Currency.SOM, "value": Currency.SOM.label}
                    ]
                },
                {
                    "label": "SteeringWheelPosition",
                    "key": [
                        {"key": SteeringWheelPosition.LEFT, "value": SteeringWheelPosition.LEFT.label},
                        {"key": SteeringWheelPosition.RIGHT, "value": SteeringWheelPosition.RIGHT.label}
                    ]
                },
                {
                    "label": "CarCondition",
                    "key": [
                        {"key": CarCondition.GOOD, "value": CarCondition.GOOD.label},
                        {"key": CarCondition.PERFECT, "value": CarCondition.PERFECT.label},
                        {"key": CarCondition.SALVAGE, "value": CarCondition.SALVAGE.label},
                        {"key": CarCondition.NEW, "value": CarCondition.NEW.label}
                    ]
                },
                {
                    "label": "MileageUnit",
                    "key": [
                        {"key": MileageUnit.KILOMETERS, "value": MileageUnit.KILOMETERS.label},
                        {"key": MileageUnit.MILES, "value": MileageUnit.MILES.label}
                    ]
                },
                {
                    "label": "AvailabilityStatus",
                    "key": [
                        {"key": AvailabilityStatus.IN_STOCK, "value": AvailabilityStatus.IN_STOCK.label},
                        {"key": AvailabilityStatus.PRE_ORDER, "value": AvailabilityStatus.PRE_ORDER.label},
                        {"key": AvailabilityStatus.IN_TRANSIT, "value": AvailabilityStatus.IN_TRANSIT.label}
                    ]
                },
                {
                    "label": "RegistrationCountry",
                    "key": [
                        {"key": RegistrationCountry.KYRGYZSTAN, "value": RegistrationCountry.KYRGYZSTAN.label},
                        {"key": RegistrationCountry.ABKHAZIA, "value": RegistrationCountry.ABKHAZIA.label},
                        {"key": RegistrationCountry.ARMENIA, "value": RegistrationCountry.ARMENIA.label},
                        {"key": RegistrationCountry.KAZAKHSTAN, "value": RegistrationCountry.KAZAKHSTAN.label},
                        {"key": RegistrationCountry.RUSSIA, "value": RegistrationCountry.RUSSIA.label},
                        {"key": RegistrationCountry.BELARUS, "value": RegistrationCountry.BELARUS.label},
                        {"key": RegistrationCountry.ANOTHER_COUNTRY,
                         "value": RegistrationCountry.ANOTHER_COUNTRY.label},
                        {"key": RegistrationCountry.NOT_REGISTERED, "value": RegistrationCountry.NOT_REGISTERED.label}
                    ]
                },
                {
                    "label": "VehicleStatus",
                    "key": [
                        {"key": VehicleStatus.RECENTLY_DELIVERED, "value": VehicleStatus.RECENTLY_DELIVERED.label},
                        {"key": VehicleStatus.TAX_PAID, "value": VehicleStatus.TAX_PAID.label},
                        {"key": VehicleStatus.INSPECTION_PASSED, "value": VehicleStatus.INSPECTION_PASSED.label},
                        {"key": VehicleStatus.NO_INVESTMENT_REQUIRED,
                         "value": VehicleStatus.NO_INVESTMENT_REQUIRED.label}
                    ]
                },
                {
                    "label": "ExchangePossibility",
                    "key": [
                        {"key": ExchangePossibility.WILL_CONSIDER_OPTIONS,
                         "value": ExchangePossibility.WILL_CONSIDER_OPTIONS.label},
                        {"key": ExchangePossibility.EXTRA_CHARGE_BUYER,
                         "value": ExchangePossibility.EXTRA_CHARGE_BUYER.label},
                        {"key": ExchangePossibility.EXTRA_CHARGE_SELLER,
                         "value": ExchangePossibility.EXTRA_CHARGE_SELLER.label},
                        {"key": ExchangePossibility.NO_ADDITIONAL_PAYMENTS,
                         "value": ExchangePossibility.NO_ADDITIONAL_PAYMENTS.label},
                        {"key": ExchangePossibility.NOT_INTERESTED, "value": ExchangePossibility.NOT_INTERESTED.label},
                        {"key": ExchangePossibility.REAL_ESTATE_EXCHANGE,
                         "value": ExchangePossibility.REAL_ESTATE_EXCHANGE.label},
                        {"key": ExchangePossibility.ONLY_EXCHANGE, "value": ExchangePossibility.ONLY_EXCHANGE.label}
                    ]
                }
            ]
        }

        return Response(data, status=200)
