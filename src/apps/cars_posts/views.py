from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import CarsPosts
from .serializers import CarsPostsSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404

from apps.helpers.paginations import StandardPaginationSet
from apps.cars_posts.filters import CarsFilters

class CarsPostsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = CarsPosts.objects.all()
    serializer_class = CarsPostsSerializer

    # pagination
    pagination_class = StandardPaginationSet

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarsFilters

    search_fields = ['description']
    ordering_fields = ['created_at', 'price']

    def get_permissions(self):
        if self.action in ['create', 'partial_update', 'destroy', 'set_active']:
            return [IsAuthenticated()]
        return [AllowAny()]


    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(user=self.request.user, context={'is_detail': False})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not instance.is_active:
            return Response({"message": "Not found."}, status=404)

        serializer = self.get_serializer(instance, context={'is_detail': True})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'is_detail': False})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={'is_detail': False})
        return Response(serializer.data)

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
