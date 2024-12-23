from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Min, Max, Q
from django.core.cache import cache

from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue,  CarColors, FilterData,
)
from .serializers import (
    CarTypeSerializer, CarMarkSerializer, CarModelSerializer, CarGenerationSerializer,
    CarSerieSerializer, CarModificationSerializer,
    CarCharacteristicValueSerializer, CarEquipmentSerializer, CarOptionSerializer,
    CarOptionValueSerializer, FuelSerializer, TransmissionSerializer, GearBoxSerializer,
    SteeringWheelSerializer, CombinedSerializer, TownsSerializer, FilterSerializer
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
                    id_car_mark=id_car_mark
                ).select_related(
                    'id_car_mark',
                    'id_car_type',
                ).order_by('name'),
                many=True).data}

            ''' filter with year (filtering with function) | output = available years'''
            if id_car_model:
                response = {
                    "type": "year",
                    "data": self.get_year(id_car_model)}

                ''' filter with year | output = generations'''
                if year:
                    # Получаем данные без уникальности
                    car_series = CarSerie.objects.filter(
                        id_car_model=id_car_model,
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
                CarMark.objects.all().order_by('name').values(), many=True).data}

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
        # cached_data = cache.get('data_list')
        
        
        # if cached_data is not None:
        #     print('================== data from cache ==================')
        #     return Response(cached_data)

        data = CombinedSerializer({
                "car_type": CarType.objects.only('id', 'name'),
                "car_condition": Condition.objects.only('id', 'name'),
                "filter_by": FilterData.objects.only('id', 'name'),
                "color": CarColors.objects.only('id', 'name', 'color'),
                "currency": Currency.objects.only('id', 'name', 'sign', 'is_default'),
                "comment_allowed": CommentAllowed.objects.only('id', 'name'),
                "configuration": GeneralOptions.objects.only('id', 'name'),
                "exterior": Exterior.objects.only('id', 'name'),
                "interior": Interior.objects.only('id', 'name'),
                "media": Media.objects.only('id', 'name'),
                "registration_country": RegistrationCountry.objects.only('id', 'name'),
                "other_option": OtherOptions.objects.only('id', 'name'),
                "gear_box": GearBox.objects.only('id', 'name'),
                "fuel": Fuel.objects.only('id', 'name'),
                "featured_option": FeaturedOption.objects.only('id', 'name'),
                "transmission": Transmission.objects.only('id', 'name'),
                "exchange": Exchange.objects.only('id', 'name'),
                "steering_wheel": SteeringWheel.objects.only('id', 'name'),
                "region": Region.objects.only('id', 'name'),
                "town": Towns.objects.only('id', 'name', 'region'),
                "safety": Safety.objects.only('id', 'name'),
        }).data

        # cache.set('data_list', data, timeout=50600)

        return Response(data)

