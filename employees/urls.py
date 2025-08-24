from rest_framework import routers
from .views import EmployeeViewSet, SkillViewSet, EmployeeSkillViewSet, WorkplaceViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'employee-skills', EmployeeSkillViewSet, basename='employee_skill')
router.register(r'workplaces', WorkplaceViewSet, basename='workplace')

urlpatterns = router.urls
