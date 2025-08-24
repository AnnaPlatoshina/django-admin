from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, TableViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'tables', TableViewSet, basename='table')

urlpatterns = [
    path('', include(router.urls)),
]
