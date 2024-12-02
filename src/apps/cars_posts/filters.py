from django_filters import FilterSet, CharFilter
from .models import CarsPosts
from django.db.models import Count, Min

# Sorting mapping with likes count and minimum price annotations
SORT_MAPPING = {
    1: '-created_at',        # Sort by created_at (descending)
    2: 'price',              # Sort by price (ascending)
    3: '-price',         # Sort by minimum price (descending)
    4: '-year',              # Sort by year (descending)
    5: 'year',               # Sort by year (ascending)
    6: '-views',             # Sort by views (descending)
    7: '-likes_count',       # Sort by likes count (descending)
    8: 'likes_count',        # Sort by likes count (ascending)
}

class CarsPostsFilter(FilterSet):
    sort = CharFilter(method='filter_sort')

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
