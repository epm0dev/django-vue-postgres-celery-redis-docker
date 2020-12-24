from django.urls import path
from .views import CarList, CarDetail


urlpatterns = [
    path('cars/', CarList.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail')
]
