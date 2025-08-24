from rest_framework import viewsets, permissions, filters
from employees.models import Employee
from .models import Table
from .serializers import EmployeeSerializer, TableSerializer

# Разрешения по ролям
class IsWatcherOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['watcher', 'admin']

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

# CRUD для сотрудников
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['skills', 'experience']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsWatcherOrAdmin]
        elif self.action in ['create', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [perm() for perm in permission_classes]

# CRUD для столов
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]
