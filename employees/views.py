from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import CustomUser


class HomeView(ListView):
    """Главная страница"""
    template_name = 'employees/home.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return CustomUser.objects.filter(is_active_employee=True)[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['description'] = 'Система управления сотрудниками компании'
        return context


class EmployeeListView(ListView):
    """Список всех сотрудников"""
    model = CustomUser
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return CustomUser.objects.filter(is_active_employee=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все сотрудники'
        return context


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """Детальная карточка сотрудника"""
    model = CustomUser
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'
    login_url = '/admin/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.get_full_name()} - Профиль'
        return context


def about_view(request):
    """Страница о проекте"""
    return render(request, 'employees/about.html', {
        'title': 'О проекте',
        'description': 'Информация о системе управления сотрудниками'
    })