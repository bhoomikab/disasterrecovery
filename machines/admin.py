from django.contrib import admin
from .models import Machine

# Register your models here.
admin.site.register(Machine)


class Machine(admin.ModelAdmin):
    list_display = ['machinename']
