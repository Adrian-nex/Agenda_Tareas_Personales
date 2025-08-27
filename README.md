# 📝 Agenda de Tareas Personales  

**Tema:** Agenda de Tareas  
**Metodologías:** Scrum + XP + GitHub + CI  

---

## 📖 Descripción  
Aplicación **CRUD en Django** que permite gestionar una **Agenda de Tareas Personales**:  

- **Título**: Nombre de la tarea  
- **Prioridad**: Alta, media o baja  
- **Estado**: Pendiente, en progreso, completada  
- **Fecha límite**: Vencimiento de la tarea  

El proyecto se desarrolló en equipo bajo **Scrum (Sprint de 2 días)** y prácticas de **XP (Pair Programming, Refactorización y TDD)**.  
Se usó **GitHub** con ramas (`main`, `caracteristicas/plantillas`, `desarrollo`), Pull Requests y **CI con GitHub Actions** para pruebas automáticas.  

---

## 👥 Equipo  
| Rol                        | Integrante        |
|----------------------------|-------------------|
| Scrum Master               | Adrian Gallardo   |
| Product Owner (Simulado)   | Camila Romero     |
| Dev Frontend (HTML + CSS)  | Leonardo Ramos    |
| Dev Frontend (HTML + CSS)  | Boris Dominguez   |
| Dev Backend (Python/Django)| Fabiano Anticona  |

---

## 🧠 Metodología  
- **Scrum**: Sprint Planning, Daily, Review, Retrospective, Backlogs e Incremento.  
- **XP**: Pair Programming, Refactorización con Class-Based Views y TDD en el modelo `Task`.  

---

### 🔑 Requisitos  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)    
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)  
![VSCode](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)  
[![Django CI](https://github.com/Adrian-nex/Agenda_Tareas_Personales/actions/workflows/django.yml/badge.svg)](https://github.com/Adrian-nex/Agenda_Tareas_Personales/actions/workflows/django.yml)

### 🚀 Pasos de Instalación 

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd agenda-tareas

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
venv\Scripts\activate

# 4. Instalar Django (si no usas requirements.txt)
pip install django

