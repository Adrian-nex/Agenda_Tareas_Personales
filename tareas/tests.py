from django.test import TestCase
from .models import Task
from datetime import date, timedelta

class TaskModelTest(TestCase):

    # ESTE METODO SE EJECUTA ANTES DE CADA TEST
    def setUp(self):
        # CREA UNA TAREA DE PRUEBA QUE NO ESTA VENCIDA (FECHA LIMITE EN 2 DIAS)
        self.task = Task.objects.create(
            title="Estudiar Django",
            priority="high",
            status="pending",
            due_date=date.today() + timedelta(days=2)
        )

    # TEST 1: VERIFICA QUE LA TAREA SE HAYA CREADA CORRECTAMENTE
    def test_task_creation(self):
        self.assertEqual(self.task.title, "Estudiar Django")
        self.assertEqual(self.task.priority, "high")
        self.assertEqual(self.task.status, "pending")
        self.assertEqual(self.task.is_overdue(), False)

    # TEST 2: VERIFICA QUE EL METODO __str__ DEVUELVA EL TITULO
    def test_str_representation(self):
        self.assertEqual(str(self.task), "Estudiar Django")

    # TEST 3: VERIFICA QUE UNA TAREA VENCIDA Y PENDIENTE DEVUELVA TRUE EN is_overdue()
    def test_is_overdue_true(self):
        overdue_task = Task.objects.create(
            title="Tarea vencida",
            priority="low",
            status="pending",
            due_date=date.today() - timedelta(days=1)
        )
        self.assertTrue(overdue_task.is_overdue())

    # TEST 4: VERIFICA QUE UNA TAREA COMPLETADA NO SEA CONSIDERADA VENCIDA
    def test_is_overdue_false_if_completed(self):
        completed_task = Task.objects.create(
            title="Tarea completada",
            priority="medium",
            status="completed",
            due_date=date.today() - timedelta(days=5)
        )
        self.assertFalse(completed_task.is_overdue())