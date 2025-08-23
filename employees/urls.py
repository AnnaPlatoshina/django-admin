from django.urls import path
from .views import employee_list, employee_detail, home

app_name = "employees"

urlpatterns = [
    path("", home, name="home"),
    path("list/", employee_list, name="employee_list"),
    path("detail/<int:pk>/", employee_detail, name="employee_detail"),
]
