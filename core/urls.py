# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register('companies', views.CompanyViewSet, basename='company')
# router.register('rooms', views.RoomsViewSet, basename='rooms')
# router.register('districts', views.DistrictViewSet, basename='district')
# router.register('markets', views.MarketViewSet, basename='market')
# router.register('prices', views.PriceViewSet, basename='price')

# urlpatterns = [
#     path('', include(router.urls)),
#     # Другие URL-адреса вашего приложения...
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('companies', views.CompanyViewSet, basename='company')
router.register('rooms', views.RoomsViewSet, basename='rooms')
router.register('districts', views.DistrictViewSet, basename='district')
router.register('markets', views.MarketViewSet, basename='market')
router.register('prices', views.PriceViewSet, basename='price')

urlpatterns = [
    path('', include(router.urls)),  # Добавляем обработку пустого пути
]

