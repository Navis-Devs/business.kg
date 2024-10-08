# packages
from django_filters import rest_framework as filters

# your import 
from apps.house import models
from apps.house import choices


class PropertyFilter(filters.FilterSet):
    location = filters.CharFilter(field_name='location__city')
    type_deal = filters.ChoiceFilter(field_name='type_deal', choices=choices.TYPE_DEAL)
    type_property = filters.ChoiceFilter(field_name='type_property', choices=choices.PROPERTY_TYPE_OPTIONS)
    room = filters.ChoiceFilter(field_name='room_count', choices=choices.ROOM_COUNT_OPTIONS)
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    year_min = filters.NumberFilter(field_name='year_construction', lookup_expr='gte', label='Год постройки от')
    year_max = filters.NumberFilter(field_name='year_construction', lookup_expr='lte', label='Год постройки до')
    currency = filters.ChoiceFilter(field_name='currency', choices=choices.CURRENCY_TYPE)
    miscellaneous = filters.BooleanFilter(field_name='documents__sale_contract', label='Наличие договора продажи')
    exchange_type = filters.ChoiceFilter(field_name='exchange_type', choices=choices.EXCHANGE_OPTIONS,
                                         label='Возможен обмен')
    mortage_type = filters.ChoiceFilter(field_name='mortage_type', choices=choices.MORTGAGE_OPTIONS,
                                        label='Возможна ипотека')
    advertiser_type = filters.ChoiceFilter(field_name='contact_info__advertiser_type',
                                           choices=choices.ADVERTISER_OPTIONS, label='От собственника')

    class Meta:
        model = models.Property
        fields = [
            'location', 'type_deal', 'type_property', 'room',
            'price_min', 'price_max', 'miscellaneous', 'year_min',
            'year_max', 'exchange_type', 'mortage_type', 'advertiser_type'
        ]
