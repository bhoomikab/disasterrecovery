from .models import Machine
from django import forms


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('machinecode', 'description', 'hourlyrent', 'max_hours_machine')
