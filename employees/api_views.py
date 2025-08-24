from rest_framework import generics, permissions, filters
from .models import Employee
from .serializers import EmployeeSerializer

# Список сотрудников с пагинацией и фильтрацией
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['skills', 'experience']

# Детальная информация о сотруднике
class EmployeeDetailAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Добавление сотрудника (только администратор)
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

# Изменение сотрудника (только администратор)
class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

# Удаление сотрудника (только администратор)
class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]
