from django.urls import include, path
from rest_framework import routers
from apps.main import views


router = routers.SimpleRouter()
router.register(r'', views.CommentView)
router.register(r"like", views.LikeViews, basename='likes')


urlpatterns = [
    path('', include(router.urls)),
    path('search/set/', views.SearchHistoryAddView.as_view()),
    path('review/', views.AdReviewView.as_view()),
    path('my-search/', views.SearchHistoryView.as_view()),
    path("dealer/", views.DealerListView.as_view()),
    path("dealer/<int:id>", views.DealerRetriveView.as_view()),
]

