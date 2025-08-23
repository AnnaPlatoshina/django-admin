from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def set_employee_username(sender, instance, created, **kwargs):
    """
    Автоматически устанавливает username на основе email,
    если username не задан
    """
    if created and not instance.username and instance.email:
        base_username = instance.email.split("@")[0]
        username = base_username
        counter = 1

        # Проверяем уникальность username
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        instance.username = username
        instance.save()
