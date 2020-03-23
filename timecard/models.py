from django.db import models


# Create your models here.

class Timecard(models.Model):
    sitecode = models.CharField(max_length=200, null=True, verbose_name="Site Code")
    contractorName = models.CharField(max_length=200, verbose_name="Contractor Name")
    total_hours = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Hours")
    total_amount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Total Amount")
    approved = models.BooleanField(default=False, verbose_name="Approval Status", )

    def __str__(self):
        return self.sitecode
