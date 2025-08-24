from rest_framework import serializers
from .models import Employee, Skill, EmployeeSkill, Workplace

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class EmployeeSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = EmployeeSkill
        fields = ['skill', 'level']

class EmployeeSerializer(serializers.ModelSerializer):
    skills = EmployeeSkillSerializer(source='employeeskill_set', many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'experience', 'skills', 'photo']

class EmployeeDetailSerializer(EmployeeSerializer):
    # Можно добавить более подробные поля при необходимости
    pass

class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ['id', 'name', 'employee']
