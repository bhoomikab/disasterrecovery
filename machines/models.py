from django.db import models


# Create your models here.

class Machine(models.Model):
    machinecode = models.CharField(max_length=200, null=True, verbose_name="Machine Code")
    description = models.TextField(verbose_name="Description")
    hourlyrent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Hourly Rent")
    max_hours_machine = models.PositiveIntegerField(verbose_name="Max Hours per day")

    def __str__(self):
        return self.machinecode
