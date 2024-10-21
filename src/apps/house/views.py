# framework packages
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# your import 
from apps.house import models
from apps.house import serializers
from apps.house import filters
from apps.helpers import paginations
from apps.helpers.permission import IsAdmin
from apps.house import mixins
from apps.house.tasks import delete_post


class ComplexView(viewsets.GenericViewSet):
    queryset = models.ResidentialCategory.objects.all()
    serializer_class = serializers.ResidentialCategorySerializer
    permission_classes = [IsAdmin, ]

    @action(detail=False, methods=['get'])
    def complexes(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CitiesView(viewsets.GenericViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.RegionsSerializer

    @action(detail=False, methods=['get'], url_path='cities')
    def cities(self, request, *args, **kwargs):
        city = request.query_params.get('town')
        all_id = request.query_params.get('all')

        if all_id:
            general_location_query = get_object_or_404(models.Location, id=all_id)
            serializer = self.get_serializer(general_location_query, context={'empty_㋡: True'})
            return Response(serializer.data, status=status.HTTP_200_OK)

        region = models.Location.objects.filter(parent=None) if not city else \
            get_object_or_404(models.Location, id=city).get_children()
        serializer = self.get_serializer(region, many=True, context={"empty_㋡": True})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PropertyView(viewsets.GenericViewSet, mixins.ViewsMixin):
    queryset = models.Property.objects.select_related(
        'location', 'documents', 'miscellaneous', 'complex_name').all().order_by('-id')
    # TODO: Prefretch to images
    serializer_class = serializers.AddPropertySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.PropertyFilter

    @action(detail=False, methods=['post'])
    def add(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            property_instance = serializer.save(user=request.user)
            if 'properties_pictures' in request.data:
                pictures_data = request.data.getlist('properties_pictures')
                for picture in pictures_data:
                    models.Pictures.objects.create(pictures=picture, property=property_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='list')
    def lists(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        paginator = paginations.PropertyResultsPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = serializers.PropertyListSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=True, methods=['get'], url_path='details')
    def details(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_views(instance=instance)
        seralizer = serializers.PropertyDetailSerializer(instance)
        return Response(seralizer.data)

    @action(detail=True, methods=['get'], url_path=None)
    def post_control(self, request, *args, **kwargs):
        instance = self.get_object()
        activate = request.query_params.get('activate', 'false').lower() == 'true'
        if activate:
            instance.active_post = True
            instance.save()
            return Response({"message ": "Post activated!"}, status=status.HTTP_200_OK)
        instance.active_post = False
        instance.save()
        instance_id = str(instance.id)
        delete_post.delay(instance_id)
        return Response({"message": "Post archived!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], url_path=None)
    def edit(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)