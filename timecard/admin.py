from django.contrib import admin
from .models import Timecard

# Register your models here.
admin.site.register(Timecard)

class Timecard(admin.ModelAdmin):
    list_display = ['timecardname']
