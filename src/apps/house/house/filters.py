# packages
from django_filters import rest_framework as filters
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django.contrib.gis.db.models import PointField

# your import 
from apps.house import models

class PropertyFilter(filters.FilterSet, GeoFilterSet):
    # GeoFilterSet
    polygon = GeometryFilter(field_name='point', lookup_expr='within')
    complex_id = filters.NumberFilter(field_name='complex_id_id')
    year_min = filters.NumberFilter(field_name='year_construction', lookup_expr='gte', label='Год постройки от')
    year_max = filters.NumberFilter(field_name='year_construction', lookup_expr='lte', label='Год постройки до')
    floor = filters.NumberFilter(field_name='floor', lookup_expr='gte', label='Этаж от')
    floors = filters.NumberFilter(field_name='floors', lookup_expr='lte', label='Этаж до')
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    video_exists = filters.BooleanFilter(field_name='youtube_url', method='filter_video_exists', label='Есть видео')
    floors_last = filters.BooleanFilter(field_name='floors', method='filter_floors_end', label='Последний этаж')
    floors_not_end = filters.BooleanFilter(field_name='floors', method='filter_floors_end', label='Не последний этаж')
    picture_exists = filters.BooleanFilter(field_name='properties_pictures', method='filter_picture_exists', label='Есть фото')
    installment = filters.BooleanFilter(field_name='installment', method='filter_possiblity', label='Возможна рассрочка')
    exchange = filters.BooleanFilter(field_name='exchange', method='filter_possiblity', label='Возможен обмен')
    mortgage = filters.BooleanFilter(field_name='mortgage', method='filter_possiblity', label='Возможна ипотека')
    order_by = filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('price', 'price'), 
        ),
        field_labels={
            'created_at': 'Дата размещения', 
            'price': 'По цене'
        },
        label='Сортировка'
    )

    def filter_video_exists(self, queryset, name, value):
        if value:
            return queryset.exclude(youtube_url__isnull=True).exclude(youtube_url__exact='')
        return queryset.filter(youtube_url__isnull=True)
    
    def filter_picture_exists(self, queryset, name, value):
        if value:
            return queryset.exclude(properties_pictures__isnull=True)
        return queryset.filter(properties_pictures__isnull=True)
    
    def filter_floors_end(self, queryset, name, value):
        if value:
            return queryset.exclude(floors=True)
        return queryset.filter(floors=True)
    
    def filter_possiblity(self, queryset, name, value):
        if value is None:
            return queryset

        if value: 
            return queryset.filter(installment__id=2)
        else:  
            return queryset.filter(installment__id=1)
        
    class Meta:
        model = models.Property
        fields = '__all__'  
        filter_overrides = {
            PointField: {
                'filter_class': GeometryFilter
            }
        }
