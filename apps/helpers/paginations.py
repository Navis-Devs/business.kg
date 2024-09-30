from rest_framework.pagination import PageNumberPagination
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