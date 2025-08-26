from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

# VISTA QUE MUESTRA UNA LISTA DE TAREAS CON POSIBILIDAD DE FILTRAR POR ESTADO O PRIORIDAD
class TaskListView(ListView):
    model = Task

    # VARIABLE QUE CONTENDRA LA LISTA EN LA PLANTILLA
    context_object_name = 'tasks'

    # RUTA DEL TEMPLATE QUE SE USARA PARA RENDERIZAR LA LISTA
    template_name = 'listar.html'
    
    # PERSONALIZAR LA CONSULTA DE OBJETOS (QUERYSET)
    def get_queryset(self):
        # OBTIENE EL QUERYSET ORIGINAL (TODAS LAS TAREAS)
        queryset = super().get_queryset()

        # OBTIENE LOS POSIBLES FILTROS DESDE LOS PARAMETROS GET DE LA URL
        status_filter = self.request.GET.get('status')
        priority_filter = self.request.GET.get('priority')
        
        # SI SE APLICO FILTRO POR ESTADO, FILTRA EL QUERYSET
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # SI SE APLICO FILTRO POR PRIORIDAD, TAMBIEN LO FILTRA
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)
        
        # DEVUELVE EL QUERYSET FINAL (FILTRADO O COMPLETO)
        return queryset

# VISTA QUE MUESTRA LOS DETALLES DE UNA SOLA TAREA
class TaskDetailView(DetailView):
    model = Task

    # VARIABLE QUE CONTENDRA EL OBJETO EN LA PLANTILLA
    context_object_name = 'task'

    # RUTA AL TEMPLATE PARA MOSTRAR LOS DETALLES DE LA TAREA
    template_name = 'detalles.html'

# VISTA QUE PERMITE CREAR UNA NUEVA TAREA USANDO UN FORMULARIO
class TaskCreateView(CreateView):
    model = Task

    # FORMULARIO A USAR (DEFINIDO EN FORMS.PY)
    form_class = TaskForm

    # TEMPLATE DONDE SE MUESTRA EL FORMULARIO
    template_name = 'formulario.html'

    # URL A LA QUE SE REDIRIGE DESPUES DE CREAR CORRECTAMENTE
    success_url = reverse_lazy('task_list')
    
    # CUANDO EL FORMULARIO ES VALIDO
    def form_valid(self, form):
        # ASIGNA AL USUARIO ACTUAL COMO PROPIETARIO DE LA TAREA
        form.instance.user = self.request.user
        
        # LLAMA AL METODO ORIGINAL PARA CONTINUAR EL PROCESO NORMAL
        return super().form_valid(form)

# VISTA QUE PERMITE EDITAR UNA TAREA EXISTENTE
class TaskUpdateView(UpdateView):
    model = Task

    # FORMULARIO A UTILIZAR
    form_class = TaskForm

    # TEMPLATE QUE SE REUTILIZA PARA EDICIÓN
    template_name = 'formulario.html'

    # REDIRIGE AL DETALLE DE LA TAREA DESPUÉS DE EDITARLA
    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

# VISTA QUE PERMITE ELIMINAR UNA TAREA EXISTENTE
class TaskDeleteView(DeleteView):
    model = Task

    # TEMPLATE PARA CONFIRMAR EL BORRADO
    template_name = 'eliminar.html'

    # REDIRIGE A LA LISTA DE TAREAS TRAS ELIMINAR LA ACTUAL
    success_url = reverse_lazy('task_list')