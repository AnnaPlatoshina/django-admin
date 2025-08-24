from django.urls import path
from .api_views import (
    EmployeeListAPIView,
    EmployeeDetailAPIView,
    EmployeeCreateAPIView,
    EmployeeUpdateAPIView,
    EmployeeDeleteAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('employees/add/', EmployeeCreateAPIView.as_view(), name='employee-add'),
    path('employees/<int:pk>/edit/', EmployeeUpdateAPIView.as_view(), name='employee-edit'),
    path('employees/<int:pk>/delete/', EmployeeDeleteAPIView.as_view(), name='employee-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
