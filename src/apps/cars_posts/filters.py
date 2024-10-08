from django.db.models import Q
from django_filters import rest_framework as filters

from apps.cars_posts.models import CarsPosts


class CarsFilters(filters.FilterSet):

    class Meta:
        model = CarsPosts
        fields = '__all__'
