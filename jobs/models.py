from django.db import models


# Create your models here.

class Jobs(models.Model):
    jobcode = models.CharField(max_length=200, null=True, verbose_name="Job Code")
    description = models.CharField(max_length=200, null=True, verbose_name="Description")
    hourlyrate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Hourly Rate")
    max_hours = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Max Hours per day")
