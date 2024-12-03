from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Exists, OuterRef


from .models import CarsPosts
from .serializers import CarsPostsDetailSerializer, CarsPostsListSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404

from apps.helpers.paginations import StandardPaginationSet
from apps.cars_posts.filters import CarsPostsFilter

class CarsPostsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
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
        return super().get_serializer_class()

    def get_queryset(self):
        if self.action == 'list':
            return CarsPosts.objects.annotate(
                    is_liked=Exists(
                        CarsPosts.likes.through.objects.filter(
                            user_id=self.request.user.id,  # Check if the current user has liked the post
                            carsposts_id=OuterRef('pk')
                        )
                    )
                ).select_related(
                    'mark', 'model'
                ).prefetch_related(
                    'pictures', 'prices', 'likes'
                )
        if self.action == 'retrieve':
            return CarsPosts.objects.all().select_related(
                'user',           # ForeignKey to Use
                'region',         # ForeignKey to Region
                'town',           # ForeignKey to Towns
                'mark',           # ForeignKey to CarMark
                'model',
                'car_type',          # ForeignKey to CarModel
                'modification_id',  # ForeignKey to CarModification
                'serie_id',       # ForeignKey to CarSerie
                'color',          # ForeignKey to CarColors
            ).prefetch_related(
                'configuration',  # ManyToMany to GeneralOptions
                'interior',        # ManyToMany to Interior
                'exterior',        # ManyToMany to Exterior
                'media',           # ManyToMany to Media
                'safety',          # ManyToMany to Safety
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
        print(self.request.data)
        serializer.save(user=self.request.user, context={'is_detail': False})


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

    @action(detail=True, methods=['patch'])
    def set_active(self, request, pk=None):
        instance = self.get_object()
        is_active = request.data.get('is_active', True)
        instance.is_active = is_active
        instance.save()
        return Response({'response': True, 'is_active': instance.is_active})
