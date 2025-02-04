from django_filters import *
from .models import CarsPosts
from django.db.models import Count, Min
from django.utils.timezone import now, timedelta

# Sorting mapping with likes count and minimum price annotations
SORT_MAPPING = {
    1: '-created_at',        # Sort by created_at (descending)
    2: 'price',              # Sort by price (ascending)
    3: '-price',         # Sort by minimum price (descending)
    4: '-views',
    5: 'year',
    6: '-year',             # Sort by views (descending)
    7: 'likes_count',       # Sort by likes count (descending)
}
# фильтрация по время размещение
TIME_CHOICES = [
    ("all", "За всё время"),
    ("day", "За последний день"),
    ("week", "За последнюю неделю"),
    ("month", "За последний месяц"),
]
SORT_OWNER = [
    ('all', 'Все'),
    ('company', 'Компания'),
    ('private', 'Частник'),
]
class CarsPostsFilter(FilterSet):
    sort_by_time = ChoiceFilter(
        choices=TIME_CHOICES,
        method="filter_by_time",
        label="Фильтрация по время размещения"
    )
    sort_by_owner = ChoiceFilter(
        choices=SORT_OWNER,
        method="filter_by_owner",
        label="Фильтрация по владельцам"
    )
    filter_by = CharFilter(method='filter_sort')
    year_min = NumberFilter(field_name='year', lookup_expr='gte', label='Год выпуска от')
    year_max = NumberFilter(field_name='year', lookup_expr='lte', label='Год выпуска до')
    horse_power_min = NumberFilter(field_name='horse_power', lookup_expr='gte', label='Л.С от')
    horse_power_max = NumberFilter(field_name='horse_power', lookup_expr='lte', label='Л.С до')
    millage_min = NumberFilter(field_name='millage', lookup_expr='gte', label='Пробег от')
    millage_max = NumberFilter(field_name='millage', lookup_expr='lte', label='Пробег до')
    price_min = NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price_max = NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    picture_exists = filters.BooleanFilter(field_name='properties_pictures', method='filter_picture_exists', label='Есть фото')
    video_exists = filters.BooleanFilter(field_name='video_url', method='filter_video_exists', label='Есть видео')

    class Meta:
        model = CarsPosts
        fields = '__all__'

    def filter_sort(self, queryset, name, value):
        try:
            sort_field = SORT_MAPPING.get(int(value))
            if sort_field:
                # Annotate the queryset with the likes count and minimum price
                if 'likes_count' in sort_field:
                    queryset = queryset.annotate(likes_count=Count('likes'))

                if 'price' == sort_field:
                    queryset = queryset.annotate(price=Min('prices__price'))
                elif sort_field == '-price':
                    queryset = queryset.annotate(price=Min('prices__price'))
                    # sort_field = '-price'

                return queryset.order_by(sort_field)
        except (ValueError, TypeError):
            pass
        return queryset
    
    def filter_by_time(self, queryset, name, value):
        if value == "day":
            return queryset.filter(created_at__gte=now() - timedelta(days=1))
        elif value == "week":
            return queryset.filter(created_at__gte=now() - timedelta(weeks=1))
        elif value == "month":
            return queryset.filter(created_at__gte=now() - timedelta(days=30))
        return queryset
    
    def filter_by_owner(self, queryset, name, value):
        if value == "company":
            return queryset.filter(dealer_id__isnull=False)
        elif value == 'private':
            return queryset.filter(dealer_id__isnull=True)
        return queryset
    
    def filter_video_exists(self, queryset, name, value):
        if value:
            return queryset.exclude(video_url__isnull=True).exclude(video_url__exact='')
        return queryset.filter(video_url__isnull=True)
    
    def filter_picture_exists(self, queryset, name, value):
        if value:
            return queryset.exclude(pictures__isnull=True)
        return queryset.filter(pictures__isnull=True)