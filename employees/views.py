from django.shortcuts import render, get_object_or_404
from .models import CustomUser, EmployeeImage, EmployeeSkill
from datetime import date


def employee_list(request):
    employees = CustomUser.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employees/employee_list.html', context)


def employee_detail(request, employee_id):
    employee = get_object_or_404(CustomUser, pk=employee_id)
    skills = EmployeeSkill.objects.filter(employee=employee)
    images = EmployeeImage.objects.filter(employee=employee).order_by('order')

    # Стаж работы в днях
    if employee.date_of_joining:
        days_at_company = (date.today() - employee.date_of_joining).days
    else:
        days_at_company = None

    context = {
        'employee': employee,
        'skills': skills,
        'images': images[1:] if images else [],  # все кроме первой
        'main_image': images[0] if images else None,
        'days_at_company': days_at_company,
    }
    return render(request, 'employees/employee_detail.html', context)
