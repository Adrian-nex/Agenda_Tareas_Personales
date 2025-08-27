from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone

class TaskForm(forms.ModelForm):
    
    # CLASE INTERNA META QUE CONFIGURA EL FORMULARIO
    class Meta:
        # MODELO EN EL QUE SE BASA EL FORMULARIO
        model = Task
        
        # CAMPOS DEL MODELO QUE SE INCLUIRAN EN EL FORMULARIO
        fields = ['title', 'description', 'priority', 'status', 'due_date']
        
        # WIDGETS HTML QUE USAN PARA RENDERIZAR ALGUNOS CAMPOS
        widgets = {
            # Renderiza due_date como un campo de tipo 'date' (selector de calendario)
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            # Renderiza description como un textarea con 4 filas
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    # VALIDACION PARA EL CAMPO due_date (FECHA LIMITE)
    def clean_due_date(self):
        # OBTIENE EL VALOR DEL CAMPO due_date DEL FORMULARIO
        due_date = self.cleaned_data.get('due_date')
        
        # SI HAY UNA FECHA Y ESTA ES ANTERIOR A HOY, LANAZR ERROR
        if due_date and due_date < timezone.now().date():
            raise ValidationError("La fecha límite no puede ser en el pasado.")
        
        # RETORNA LA FECHA VALIDADA
        return due_date