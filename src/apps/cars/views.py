from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Min, Max, Q

from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue,  CarColors
)
from .serializers import (
    CarTypeSerializer, CarMarkSerializer, CarModelSerializer, CarGenerationSerializer,
    CarSerieSerializer, CarModificationSerializer,
    CarCharacteristicValueSerializer, CarEquipmentSerializer, CarOptionSerializer,
    CarOptionValueSerializer, FuelSerializer, TransmissionSerializer, GearBoxSerializer,
    SteeringWheelSerializer, CombinedSerializer, TownsSerializer
)

from apps.cars_posts.models import (
    Transmission,
    Fuel,
    Towns,
    GearBox,
    SteeringWheel,
    CarMark,
    CarModel,
    CarType,
    Region,
    Exchange,
    Towns,
    RegistrationCountry,
    CommentAllowed,
    Transmission, 
    Currency,
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
        car_serie = request.query_params.get("serie")
        car_fuel = request.query_params.get("fuel")
        transmission = request.query_params.get("transmission")
        modification = request.query_params.get('modification')
        steering_wheel = request.query_params.get('steering_wheel')
        gear_box = request.query_params.get("gear_box")
        # example request : http://localhost/cars-data/parameters/?mark=76&model=753&year=1996&serie=6312&generation=9349&fuel=%D0%91%D0%B5%D0%BD%D0%B7%D0%B8%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9&transmission=%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9&gear_box=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82&engine=2156
        ''' filter with mark | output = marks'''
        if id_car_mark:
            response = {
                "type": "model",
                "data": CarModelSerializer(
                CarModel.objects.filter(
                    id_car_mark__id=id_car_mark
                ), many=True).data}

            ''' filter with year (filtering with function) | output = available years'''
            if id_car_model:
                response = {
                    "type": "year",
                    "data": self.get_year(id_car_model)}

                ''' filter with year | output = generations'''
                if year:
                    # Получаем данные без уникальности
                    car_series = CarSerie.objects.filter(
                        id_car_model__id=id_car_model,
                        id_car_generation__year_end__gte=year,
                        id_car_generation__year_begin__lte=year
                    )

                    serialized_data = CarSerieSerializer(car_series, many=True).data

                    unique_data = []
                    seen_names = set()

                    for item in serialized_data:
                        name = item.get('name')
                        if name not in seen_names:
                            seen_names.add(name)
                            unique_data.append(item)

                    response = {
                        "type": "series",
                        "data": unique_data
                    }

                    ''' filter with serie | output = generation '''
                    if car_serie:
                        response = {
                            "type": "generation",
                            "data": CarGenerationSerializer(
                                CarGeneration.objects.filter(
                                    id_car_model__id=id_car_model,
                                    year_end__gte=year,
                                    year_begin__lte=year,
                                    car_serie=car_serie
                                ).order_by("year_begin"), many=True).data}

                        ''' filter with generation | output = fuel type '''
                        if id_car_generation:    
                            inst = Fuel.objects.all()  
                            ser = FuelSerializer(inst, many=True)
                            response = {
                                "type": "fuels",
                                "data": ser.data
                            }

                            ''' filter with car_fuel | output = transmission '''
                            if car_fuel:
                                q = Transmission.objects.all()
                                s = TransmissionSerializer(q, many=True).data
                                response = {
                                    "type": "transmission",
                                    "data": s
                                }

                                ''' filter with transmission | output = gear_box '''
                                if transmission:
                                    q = GearBox.objects.all()
                                    s = GearBoxSerializer(q, many=True).data
                                    response = {
                                        "type": "gear_box",
                                        "data":s
                                    }

                                    ''' filter with gear_box '''
                                    if gear_box:
                                        response = {
                                                "type": "modification",
                                                "data": CarModificationSerializer(
                                                    CarModification.objects.filter(
                                                        id_car_model=id_car_model,
                                                        id_car_serie=car_serie
                                                    ), many=True).data}
                                        if modification:
                                            response = {
                                                "type": "steering_wheel",
                                                "data": SteeringWheelSerializer(
                                                    SteeringWheel.objects.all(),
                                                    many=True
                                                ).data
                                            }
                                            if steering_wheel:
                                                return Response({"output": "success"}, status=status.HTTP_200_OK)


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


class DataView(generics.GenericAPIView):
    def get(self, request):
        region_id = request.query_params.get('region_id')

        if region_id:
            towns_queryset = Towns.objects.filter(region_id=region_id)
            towns_serializer = TownsSerializer(towns_queryset, many=True)
            return Response({"town": towns_serializer.data})   
                    
        car_type = CarType.objects.all()
        car_condition = Condition.objects.all()
        color = CarColors.objects.all()
        currency = Currency.objects.all()
        comment_allowed = CommentAllowed.objects.all()
        configuration = GeneralOptions.objects.all()
        exterior = Exterior.objects.all()
        interior = Interior.objects.all()
        media = Media.objects.all()
        registration_country = RegistrationCountry.objects.all()
        other_option = OtherOptions.objects.all()
        gear_box = GearBox.objects.all()
        fuel = Fuel.objects.all()
        featured_option = FeaturedOption.objects.all()
        transmission = Transmission.objects.all()
        exchange = Exchange.objects.all()
        steering_wheel = SteeringWheel.objects.all()
        region = Region.objects.all()
        data = CombinedSerializer({
            "car_type": car_type,
            "car_condition": car_condition,
            "color": color,
            "currency": currency,
            "comment_allowed": comment_allowed,
            "configuration": configuration,
            "exterior": exterior,
            "registration_country": registration_country,
            "interior": interior,
            "media": media,
            "other_option": other_option,
            "gear_box": gear_box,
            "fuel": fuel,
            "featured_option": featured_option,
            "transmission": transmission,
            "exchange": exchange,
            "steering_wheel": steering_wheel,
            "region": region
        }).data

        return Response(data)