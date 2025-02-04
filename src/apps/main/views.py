from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.main import models
from django.db.models import Count, Avg, F
from apps.accounts.models import User
from apps.main import serializers
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import views
from django.utils.translation import gettext_lazy as _
from apps.helpers.paginations import StandardPaginationSet

from .serializers import (
    DealerListSerializer,
    DealerSerializer
)
from apps.accounts.models import (
    Dealer
)


# data
''' cars '''
from apps.cars_posts.models import CarsPosts
from apps.cars_posts.serializers import CarsPostsListSerializer

''' houses '''
from apps.house.models import Property
from apps.house.serializers import PropertySerializer
from itertools import chain

class SearchHistoryAddView(generics.CreateAPIView):
    queryset = models.SearchHistory.objects.all()
    serializer_class = serializers.SearchHistorySerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SearchHistoryView(generics.ListAPIView):
    queryset = models.SearchHistory.objects.all()
    serializer_class = serializers.SearchHistorySerializer
    pagination_class = None
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        query_type = self.request.query_params.get("type")
        if not query_type:
            return models.SearchHistory.objects.all()
        return models.SearchHistory.objects.filter(type=query_type)

class SearchHistoryDestroyView(views.APIView):
    permission_classes = [IsAuthenticated,]
    
    def delete(self, request, id):
        user = request.user
        q = get_object_or_404(models.SearchHistory, user=user, id=id)
        q.delete()
        return Response({"message": _("Сохраненный поиск удален!")}, status=status.HTTP_200_OK)
    
class AdReviewView(generics.CreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
class CommentView(viewsets.GenericViewSet):
    queryset = models.Comments.objects.all().order_by('-id')
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated,]

    @action(detail=False, methods=['post'])
    def create_comment(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "comment succes created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        type = self.kwargs.get("type")
        if type == "car":
            return CarsPosts.objects.all()
        if type == "house":
            return Property.objects.all()
        return None

    @action(detail=True, methods=["get"], url_path='(?P<type>house|car)/set_like')
    def set_like(self, request, pk=None, type=None):
        instance = self.get_object()
        if instance is None:
            return Response({"error": "Не валидный тип"}, status=400)

        instance.likes.add(request.user)
        instance.save()
        return Response({"response": True, "message": "Лайк добавлен успешно!"})

    @action(detail=True, methods=["get"], url_path='(?P<type>house|car)/remove_like')
    def remove_like(self, request, pk=None, type=None):
        instance = self.get_object()
        if instance is None:
            return Response({"response": False, "error": "Неверный тип"}, status=400)

        instance.likes.remove(request.user)
        instance.save()
        return Response({"response": True, "message": "Лайк был успешно удалён!"})

    @action(detail=False, methods=["get"], url_path="my_favorites")
    def my_favorites(self, request):
        user = request.user

        ''' cars data '''
        car_favorites = CarsPosts.objects.filter(likes=user)
        cars_serializer = CarsPostsListSerializer(car_favorites, many=True, context={'request': request}).data

        ''' house data '''
        house_favorites = Property.objects.filter(likes=user)
        house_serializer = PropertySerializer(house_favorites, many=True, context={'request': request}).data

        ''' merge all data and sorting with key "created_at" '''
        return Response({
            "cars": cars_serializer,
            "houses": house_serializer
        })


class DealerListView(generics.GenericAPIView):
    queryset = Dealer.objects.all().order_by('id')
    serializer_class = DealerListSerializer
    pagination_class = StandardPaginationSet
    
    def get(self, request):
        type = request.query_params.get('type_dealer')
        query = Dealer.objects.filter(type_dealer=type).select_related('user')
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get_queryset(self):
    #     return Dealer.objects.filter(type_dealer=type_dealer).select_related('user').annotate(
    #         average_rating=Avg('reviews__rating'),
    #         property_count=Count('property', distinct=True),
    #         carsposts_count=Count('carsposts', distinct=True),
    #         accommodation_count=F('property_count') + F('carsposts_count')
    #     )

class DealerRetriveView(generics.RetrieveAPIView):
    queryset = Dealer.objects.all().order_by('-id').select_related('user')
    serializer_class = DealerSerializer
    pagination_class = StandardPaginationSet
    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        dealer = self.get_object()  
        user = dealer.user
        
        if dealer.type_dealer == 'car':
            ads = CarsPostsListSerializer(CarsPosts.objects.filter(user=user).select_related('car_type'), many=True, context={'request': request}).data
        else:
            ads = PropertySerializer(Property.objects.filter(user=user), many=True, context={'request': request}).data
        
        # ads = {"house": property_data, "car": car_data}
        
        data = self.serializer_class(dealer).data
        data["dates"] = {
            "date_joined": f"{user.date_joined}",
            "last_login": f"{user.last_login}",
            "ads": ads
        }

        return Response(data)