from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    hire_date = models.DateField(
        verbose_name=_('Дата приёма на работу'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')