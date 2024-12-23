from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Exists, OuterRef
from django.db.models import Count, Avg, F


from .models import CarsPosts, Pictures, User, CarPrices
from .serializers import CarsPostsDetailSerializer, CarsPostsListSerializer, AdCarsPostsSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404

from apps.helpers.paginations import StandardPaginationSet
from apps.cars_posts.filters import CarsPostsFilter
from apps.house.mixins import ViewsMixin as CustomMixin

class CarsPostsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       CustomMixin,
                       viewsets.GenericViewSet):

    # pagination
    pagination_class = StandardPaginationSet

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarsPostsFilter

    search_fields = ['description']
    ordering_fields = ['created_at', 'price']
    serializer_class = CarsPostsDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CarsPostsListSerializer
        if self.action == 'create':
            return AdCarsPostsSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        if self.action == 'list':
            return CarsPosts.objects.annotate(
                    is_liked=Exists(
                        CarsPosts.likes.through.objects.filter(
                            user_id=self.request.user.id,  
                            carsposts_id=OuterRef('pk')
                        )
                    )
                ).select_related(
                    'mark', 'model'
                ).prefetch_related(
                    'pictures', 'prices', 'likes'
                ).order_by('-is_vip', '-is_premium', '-is_top', '-is_autoup')
                
        if self.action == 'retrieve':
            return CarsPosts.objects.all().select_related(
                'user',     
                'region',   
                'town',     
                'mark',     
                'model',
                'car_type',          
                'modification_id',  
                'serie_id',       
                'color',         
            ).prefetch_related(
                'configuration',  
                'interior',  
                'exterior',  
                'media',  
                'safety',  
                'other_options',
                'pictures',
                'prices',
                'likes'
            )
        return super().get_queryset()
    

    def get_permissions(self):
        if self.action in ['create', 'partial_update', 'destroy', 'set_active']:
            return [IsAuthenticated()]
        return [AllowAny()]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def partial_update(self, request, *args, **kwargs):
        restricted_fields = {'user', 'id', 'car_type', 'mark', 'model'}
        for field in restricted_fields:
            if field in request.data:
                return Response(
                    {"error": f"Updating '{field}' is not allowed."},
                    status=400
                )
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=204)
    
    def create(self, request, *args, **kwargs):
        pictures_files = request.FILES.getlist('pictures')  
        price = request.data.get('price')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car_post = serializer.save(user=request.user)

        if pictures_files:
            pictures_instances = [
                Pictures(cars=car_post, pictures=picture) for picture in pictures_files
            ]
            Pictures.objects.bulk_create(pictures_instances)
        if price:
            CarPrices.objects.create(cars=car_post, price=price)
            CarPrices.objects.create(cars=car_post, price=price)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_views(instance)  
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
