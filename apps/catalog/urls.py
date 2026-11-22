from .views import FlowerViewSet, FlowerGradeViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flowers', FlowerViewSet)
router.register(r'flower-grades', FlowerGradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]