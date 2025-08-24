from rest_framework import serializers
from employees.models import Employee
from .models import Table

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
