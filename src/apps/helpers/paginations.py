from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response


class StandardPaginationSet(PageNumberPagination):
    limit = 20
    page_size_query_param = 'limit'
    max_page_size = 1000

    def get_paginated_response(self, data):
        try:
            limit = int(self.request.GET.get('limit', self.limit))
        except ValueError:
            limit = self.limit
        # limit = min(page_size, self.limit)
        return Response(
            {
                'page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'limit': limit,
                'total_count': self.page.paginator.count,
                'data': data,
            }
        )

# class StandardPaginationSet(LimitOffsetPagination):
#     default_limit = 10  # Default limit if no limit is specified
#     max_limit = 100     # Maximum limit allowed

#     # Optionally, you can also customize the query parameter name:
#     limit_query_param = 'limit'  # By default it's 'limit', but can be changed.
#     offset_query_param = 'offset' 