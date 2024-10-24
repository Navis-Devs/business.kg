from rest_framework import generics, views
from rest_framework.response import Response
from .models import TariffPlan


class TariffPlanView(views.APIView):
    def get(self, request):
        objects = TariffPlan.objects.all()

        response_data = {
            'basic': {},
            'advanced': {},
            'expert': {}
        }

        for obj in objects:
            key = obj.name.lower()

            duration_key = obj.duration_days

            if duration_key not in response_data[key]:
                response_data[key][duration_key] = []

            response_data[key][duration_key].append({
                'id': obj.id,
                # 'name': obj.name,
                'price': obj.price,
                'duration_days': obj.duration_days,
                'limit': obj.limit,
                'own_branded_page': obj.own_branded_page,
                'auto_up': obj.auto_up,
                'placement_on_main_page': obj.placement_on_main_page,
                'tag_with_company_name': obj.tag_with_company_name,
                'no_ad_photos': obj.no_ad_photos,
                'without_competitors': obj.without_competitors,
                'search_by_ads': obj.search_by_ads,
            })

        return Response(response_data, status=200)
