from django.db import models
from django.urls import reverse
from django.utils import timezone

# MODELO TAREA
class Task(models.Model):
    # OPCIONES PARA EL CAMPO PRIORITY (PRIORIDAD)
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
    ]
    
    # OPCIONES PARA EL CAMPO STATUS (ESTADO)
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completada'),
    ]
    
    # CAMPO DE TEXTO CORTO PARA EL TITULO DE LA TAREA
    title = models.CharField(max_length=100, verbose_name="Título")
    
    # CAMPO DE TEXTO LARGO OPCIONAL PARA UNA DESCRIPCION DE LA TAREA
    description = models.TextField(blank=True, verbose_name="Descripción")
    
    # PRIORIDAD DE LA TAREA, CON OPCIONES DEFINIDAS Y VALOR POR DEFECTO MEDIUM (MEDIA)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name="Prioridad")
    
    # ESTADO ACTUAL DE LA TAREA, CON OPCIONES DEFINIDAS Y VALOR POR DEFECTO PENDING (PENDIENTE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending', verbose_name="Estado")
    
    # FECHA LIMITE PARA COMPLETAR LA TAREA
    due_date = models.DateField(verbose_name="Fecha Límite")
    
    # FECHA Y HORA EN QUE SE CREO LA TAREA (AUTOMATICAMENTE ASIGNADA AL CREAR)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # FECHA Y HORA EN QUE SE ACTUALIZO LA TAREA POR ULTIMA VEZ (AUTOMATICAMENTE ASIGNADA AL GUARDAR)
    updated_at = models.DateTimeField(auto_now=True)
    
    # METADATOS DEL MODELO (INFORMACION Y ESTRUCUTURA)
    class Meta:
        ordering = ['-priority', 'due_date']
    
    # REPRESENTACION EN TEXTO DEL OBJETO (EN EL ADMIN DE DJANGO)
    def __str__(self):
        return self.title
    
    # DEVUELVE LA URL ABSOLUTA PARA VER LOS DETALLES DE ESTA TAREA
    def get_absolute_url(self):
        # USA EL NOMBRE DE LA VISTA 'task_detail' Y PASA EL ID (PRIMARY KEY) DE LA TAREA
        return reverse('task_detail', kwargs={'pk': self.pk})
    
    # DEVUELVE TRUE SI LA TAREA ESTA VENCIDA (FECHA LIMITE PASADA Y NO COMPLETADA)
    def is_overdue(self):
        # SOLO CONSIDERA UNA TAREA COMO VENCIDA SI NO ESTA COMPLETADA
        return self.due_date < timezone.now().date() if self.status != 'completed' else False