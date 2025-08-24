# employees/serializers.py

from rest_framework import serializers
from .models import Employee, Skill, EmployeeSkill, Workplace, EmployeeImage, CustomUser

# Сериализатор для сотрудников
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Сериализатор для навыков
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

# Сериализатор для связи сотрудников и навыков
class EmployeeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSkill
        fields = '__all__'

# Сериализатор для рабочих мест
class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'

# Если у тебя есть кастомные пользователи
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# Для изображений сотрудников (если используешь ImageField)
class EmployeeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeImage
        fields = '__all__'
