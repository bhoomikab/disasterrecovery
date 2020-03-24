from django.db import models


# Create your models here.

class Job(models.Model):
    jobcode = models.CharField(max_length=200, null=True, verbose_name="Job Code")
    description = models.TextField(verbose_name="Description")
    hourlyrate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Hourly Rate")
    max_hours = models.PositiveIntegerField(verbose_name="Max Hours per day")

    def __str__(self):
        return self.jobcode
