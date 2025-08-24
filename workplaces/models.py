from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=50)
    max_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name
