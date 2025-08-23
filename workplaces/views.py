from django.shortcuts import render
from django.db.models import Q
from .models import CustomUser, Skill


def employee_list(request):
    employees = CustomUser.objects.all()

    # --- фильтрация ---
    department = request.GET.get('department')
    skill = request.GET.get('skill')
    min_experience = request.GET.get('min_experience')
    sort_by = request.GET.get('sort', 'last_name')

    if department:
        employees = employees.filter(department__icontains=department)

    if skill:
        employees = employees.filter(employee_skills__skill__name__icontains=skill).distinct()

    if min_experience:
        try:
            min_exp = int(min_experience)
            employees = [
                e for e in employees if e.work_experience_days >= min_exp * 365
            ]
        except ValueError:
            pass

    # --- сортировка ---
    if sort_by in ['last_name', 'first_name', 'hire_date']:
        employees = employees.order_by(sort_by)

    context = {
        'employees': employees,
        'departments': CustomUser.objects.values_list('department', flat=True).distinct(),
        'skills': Skill.objects.all(),
    }
    return render(request, 'employee_list.html', context)
