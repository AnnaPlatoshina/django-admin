from django.contrib import admin
from .models import CustomUser, Skill, EmployeeSkill, EmployeeImage

admin.site.register(CustomUser)
admin.site.register(Skill)
admin.site.register(EmployeeSkill)
admin.site.register(EmployeeImage)
