# framework packages
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from apps.house import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework import mixins as rest_mixin
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from django.db import connection


# your import 
from apps.house import models
from apps.house import serializers
from apps.house import data_serializers
from apps.house import data_models
from apps.house import filters
from apps.helpers import paginations
from apps.house import mixins
from apps.house import choices
from apps.house.tasks import delete_post
from apps.house import exceptions


class ComplexView(viewsets.GenericViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingsSerializer
    pagination_class = paginations.StandardPaginationSet
    
    @action(detail=False, methods=['get'])
    def buildings(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def building(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add_buildings(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "complex succes created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PropertyView(
        rest_mixin.ListModelMixin,
        rest_mixin.RetrieveModelMixin,
        viewsets.GenericViewSet,
        rest_mixin.CreateModelMixin,
        mixins.ViewsMixin
    ):
    queryset = models.Property.objects.select_related(
    'user', 'category', 'type_id', 'region', 'town', 'district', 'microdistrict', 'complex_id', 'dealer_id',
    ).prefetch_related(
        'land_amenities', 'options', 'safety', 'land_options',
        'room_options', 'flat_options', 'documents',
        ).order_by('-is_vip', '-is_premium', '-is_top', '-is_autoup')
    serializer_class = serializers.AddPropertySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.PropertyFilter
    pagination_class = paginations.StandardPaginationSet
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.AddPropertySerializer
        if self.action == 'list':
            return serializers.PropertyListSerializer
        return serializers.PropertySerializer
    
    @action(detail=True, methods=['patch'], url_path=None)
    def edit(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)
            # {
            #     "outcome": "success",
            #     "ad_id": response.data.get('id'),
            #     "status": response.status_code,
            #     "data": response.data
            #     },    
            # status=status.HTTP_201_CREATED
        # )
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_views(instance)  
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class DataView(APIView):
    # serializer_class = data_serializers.CombinedSerializer

    # def get(self, request):
    #     cached_data = cache.get('data_list')
    #     if cached_data is not None:
    #         print('================== data from cache ==================')
    #         return Response(cached_data)

    #     data = {
    #         'type': list(data_models.Type.objects.values("translations__name")),
    #         'category': list(data_models.Category.objects.values()),
    #         'rooms': list(data_models.Rooms.objects.values()),
    #         'material': list(data_models.Material.objects.values()),
    #         'floors': list(data_models.Floor.objects.values()),
    #         'condition': list(data_models.Condition.objects.values()),
    #         'owner_type': list(data_models.AccountType.objects.values()),
    #         'heating': list(data_models.Heating.objects.values()),
    #         'region': list(data_models.Region.objects.values()),
    #         'irrigation': list(data_models.Irrigation.objects.values()),
    #         'land_options': list(data_models.LandOptions.objects.values()),
    #         'land_location': list(data_models.LandLocation.objects.values()),
    #         'rental_term': list(data_models.RentalTerm.objects.values()),
    #         'land_amenities': list(data_models.LandAmenities.objects.values()),
    #         'room_option': list(data_models.RoomOption.objects.values()),
    #         'water': list(data_models.Water.objects.values()),
    #         'electricity': list(data_models.Electricity.objects.values()),
    #         'options': list(data_models.Options.objects.values()),
    #         'building_type': list(data_models.BuildingType.objects.values()),
    #         'finishing': list(data_models.Finishing.objects.values()),
    #         'canalization': list(data_models.Canalization.objects.values()),
    #         'comment_allowed': list(data_models.CommentAllowed.objects.values()),
    #         'parking_type': list(data_models.ParkingType.objects.values()),
    #         'commercial_type': list(data_models.CommercialType.objects.values()),
    #         'room_location': list(data_models.RoomLocation.objects.values()),
    #         'phone_info': list(data_models.Phone.objects.values()),
    #         'internet': list(data_models.Internet.objects.values()),
    #         'toilet': list(data_models.Toilet.objects.values()),
    #         'gas': list(data_models.Gas.objects.values()),
    #         'balcony': list(data_models.Balcony.objects.values()),
    #         'door': list(data_models.Door.objects.values()),
    #         'parking': list(data_models.Parking.objects.values()),
    #         'furniture': list(data_models.Furniture.objects.values()),
    #         'flooring': list(data_models.Flooring.objects.values()),
    #         'safety': list(data_models.Safety.objects.values()),
    #         'flat_options': list(data_models.FlatOptions.objects.values()),
    #         'exchange': list(data_models.Exchange.objects.values()),
    #         'price_type': list(data_models.PriceType.objects.values()),
    #         'currency': list(data_models.Currency.objects.values()),
    #         'possibility': list(data_models.Possibility.objects.values()),
    #         'document': list(data_models.Document.objects.values()),
    #         'serie': list(data_models.Serie.objects.values()),
    #         'district': list(data_models.District.objects.values()),
    #         'microdistrict': list(data_models.MicroDistrict.objects.values()),
    #         'town': list(data_models.Town.objects.values())
    #     }

    #     cache.set('data_list', data, timeout=78796800)

    #     return Response(data)
    
    serializer_class = data_serializers.CombinedSerializer
    
    def get(self, request):
        # cached_data = cache.get('house_public')
        # if cached_data is not None:
        #     print('================== data from cache ==================')
        #     return Response(cached_data)
        
        data = {
            'type': data_models.Type.objects.all(),
            'category': data_models.Category.objects.all(),
            'rooms': data_models.Rooms.objects.all(),
            'material': data_models.Material.objects.all(),
            'floors': data_models.Floor.objects.all(),
            'condition': data_models.Condition.objects.all(),
            'owner_type': data_models.AccountType.objects.all(),
            'heating': data_models.Heating.objects.all(),
            'region': data_models.Region.objects.all(),
            'irrigation': data_models.Irrigation.objects.all(),
            'land_options': data_models.LandOptions.objects.all(),
            'land_location': data_models.LandLocation.objects.all(),
            'rental_term': data_models.RentalTerm.objects.all(),
            'land_amenities': data_models.LandAmenities.objects.all(),
            'room_option': data_models.RoomOption.objects.all(),
            'water': data_models.Water.objects.all(),
            'electricity': data_models.Electricity.objects.all(),
            'options': data_models.Options.objects.all(),
            'building_type': data_models.BuildingType.objects.all(),
            'finishing': data_models.Finishing.objects.all(),
            'canalization': data_models.Canalization.objects.all(),
            'comment_allowed': data_models.CommentAllowed.objects.all(),
            'parking_type': data_models.ParkingType.objects.all(),
            'commercial_type': data_models.CommercialType.objects.all(),
            'room_location': data_models.RoomLocation.objects.all(),
            'phone_info': data_models.Phone.objects.all(),
            'internet': data_models.Internet.objects.all(), 
            'toilet': data_models.Toilet.objects.all(),
            'gas': data_models.Gas.objects.all(),
            'balcony': data_models.Balcony.objects.all(),
            'door': data_models.Door.objects.all(),
            'parking': data_models.Parking.objects.all(),
            'furniture': data_models.Furniture.objects.all(),
            'flooring': data_models.Flooring.objects.all(),
            'safety': data_models.Safety.objects.all(),
            'flat_options': data_models.FlatOptions.objects.all(),
            'exchange': data_models.Exchange.objects.all(),
            'price_type': data_models.PriceType.objects.all(),
            'currency': data_models.Currency.objects.all(),
            'possibility': data_models.Possibility.objects.all(),
            'document': data_models.Document.objects.all(),
            'serie': data_models.Serie.objects.all(),
            'district': data_models.District.objects.all(),
            'town': data_models.Town.objects.all(),
            'microdistrict': data_models.MicroDistrict.objects.all()
        }
        
        serializer = self.serializer_class(data)
        # cache.set('house_public', serializer.data, timeout=3600)
        return Response(serializer.data)

    

class PropertyParam(APIView):
    def get(self, request):

        validation_result = self.validate_params(request)
        
        if 'error' in validation_result:
            return Response(validation_result, status=status.HTTP_200_OK)
        
        return Response({"success": "Все параметры валидны"}, status=status.HTTP_200_OK)

    def validate_params(self, request):
        type_id = request.query_params.get('type_id')
        category = request.query_params.get('category')
        region_id = request.query_params.get('region_id')  
        town_id = request.query_params.get('town_id')
        
        rules = exceptions.get_validation_rules(region_id, town_id).get(type_id, {}).get(category)
        print(f"Validation rules: {rules}")
        if not rules:
            return {"error": "Параметры не указаны type_id & category", "developer_message": "Введите идентификатор типа и категорий", "client_message": "Пожайлуста, заполните все обезятельые поля!"}

        missing_fields = []
        invalid_fields = []

        for rule in rules:
            field_name = rule['label']
            required = rule.get('required', False)
            value = request.query_params.get(field_name)

            if required and not value :
                missing_fields.append(field_name)

        available_fields = [
            {
                "label": rule['label'],
                "type": rule['type'],
                "title": rule['title'],
                "placeholder": rule['placeholder'],
                "required": rule['required'],
                "input": rule['input'],
            }
            for rule in rules
        ]

        response = {}
        if missing_fields:
            response.update({
                "error": "Missing required fields",
                "missing_fields": missing_fields,
            })
        if invalid_fields:
            response.update({
                "error": "Invalid fields",
                "invalid_fields": invalid_fields,
            })

        response["available_fields"] = available_fields
        return response if response else {"success": "All fields are valid"}