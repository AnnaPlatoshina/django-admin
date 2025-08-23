from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'

    def ready(self):
        # Импортируем сигналы здесь, чтобы избежать двойной регистрации
        import employees.signals