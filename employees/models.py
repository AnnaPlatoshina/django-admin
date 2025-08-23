from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import default_storage

# Импортируем CKEditor 5 для WYSIWYG редактора
try:
    from django_ckeditor_5.fields import CKEditor5Field
except ImportError:
    # Fallback на обычное TextField если CKEditor 5 не установлен
    CKEditor5Field = models.TextField


class Skill(models.Model):
    """Модель для навыков сотрудников"""
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название навыка'),
        help_text=_('Например: Фронтенд, Бэкенд, Тестирование')
    )
    category = models.CharField(
        max_length=100,
        verbose_name=_('Категория'),
        blank=True,
        help_text=_('Категория навыка (технический, управленческий и т.д.)')
    )
    description = models.TextField(
        verbose_name=_('Описание навыка'),
        blank=True
    )

    class Meta:
        verbose_name = _('Навык')
        verbose_name_plural = _('Навыки')
        ordering = ['name']

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    """Промежуточная модель для связи сотрудник-навык с уровнем"""
    employee = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
        related_name='employee_skills',
        verbose_name=_('Сотрудник')
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        verbose_name=_('Навык')
    )
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name=_('Уровень навыка (1-10)'),
        help_text=_('Оценка от 1 (начальный) до 10 (эксперт)')
    )
    experience_years = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0,
        verbose_name=_('Опыт (лет)'),
        help_text=_('Количество лет опыта с этим навыком')
    )
    last_used = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Последнее использование'),
        help_text=_('Когда в последний раз использовался этот навык')
    )

    class Meta:
        verbose_name = _('Навык сотрудника')
        verbose_name_plural = _('Навыки сотрудников')
        unique_together = ['employee', 'skill']
        ordering = ['-level', 'skill__name']

    def __str__(self):
        return f"{self.employee} - {self.skill} (уровень {self.level})"


class EmployeeImage(models.Model):
    """Модель для изображений сотрудника"""
    employee = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Сотрудник')
    )
    image = models.ImageField(
        upload_to='employee_images/%Y/%m/%d/',
        verbose_name=_('Изображение')
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Порядковый номер'),
        help_text=_('Чем меньше число, тем раньше отображается изображение')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))

    class Meta:
        verbose_name = _('Изображение сотрудника')
        verbose_name_plural = _('Изображения сотрудников')
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"Изображение {self.employee.get_full_name()} (#{self.order})"

    def delete(self, *args, **kwargs):
        """Удаляем файл изображения при удалении записи"""
        if self.image:
            if default_storage.exists(self.image.name):
                default_storage.delete(self.image.name)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        """Автоматически устанавливаем порядок, если не указан"""
        if self.order == 0:
            # Находим максимальный порядок для этого сотрудника и добавляем 1
            max_order = EmployeeImage.objects.filter(
                employee=self.employee
            ).aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)


class CustomUser(AbstractUser):
    """Расширенная модель пользователя для сотрудников"""

    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Мужской')
        FEMALE = 'F', _('Женский')
        OTHER = 'O', _('Другой')
        PREFER_NOT_TO_SAY = 'N', _('Не указано')

    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.PREFER_NOT_TO_SAY,
        verbose_name=_('Пол')
    )

    middle_name = models.CharField(
        max_length=150,
        verbose_name=_('Отчество'),
        blank=True,
        help_text=_('При наличии')
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Дата рождения'),
        help_text=_('Формат: ГГГГ-ММ-ДД')
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('Телефон'),
        help_text=_('Контактный телефон')
    )

    hire_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Дата приема на работу'),
        help_text=_('Когда сотрудник был принят на работу')
    )

    position = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_('Должность'),
        help_text=_('Текущая должность сотрудника')
    )

    department = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_('Отдел'),
        help_text=_('Отдел или подразделение')
    )

    description = CKEditor5Field(
        verbose_name=_('Описание'),
        blank=True,
        help_text=_('Подробное описание сотрудника, опыт работы, достижения'),
        config_name='extends'
    )

    is_active_employee = models.BooleanField(
        default=True,
        verbose_name=_('Активный сотрудник'),
        help_text=_('Отметьте, если сотрудник работает в компании')
    )

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        parts = [self.last_name, self.first_name]
        if self.middle_name:
            parts.append(self.middle_name)
        return ' '.join(parts)

    def get_full_name(self):
        """Возвращает полное имя сотрудника с отчеством"""
        full_name = super().get_full_name()
        if self.middle_name:
            full_name += f' {self.middle_name}'
        return full_name

    def get_short_name(self):
        """Возвращает краткое имя сотрудника"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name[0]}."
        return self.username

    @property
    def primary_skills(self):
        """Основные навыки сотрудника (уровень ≥ 7)"""
        return self.employee_skills.filter(level__gte=7).select_related('skill')

    @property
    def skill_count(self):
        """Количество навыков сотрудника"""
        return self.employee_skills.count()

    def get_skill_level(self, skill_name):
        """Получить уровень конкретного навыка"""
        try:
            return self.employee_skills.get(skill__name=skill_name).level
        except EmployeeSkill.DoesNotExist:
            return None

    @property
    def sorted_images(self):
        """Возвращает изображения сотрудника в правильном порядке"""
        return self.images.all().order_by('order')

    @property
    def primary_image(self):
        """Возвращает первое изображение для превью"""
        return self.images.first()