from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse

from .forms import TaskForm, ProjectForm
from .models import Project, Task

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)
def register(request):
    """Registro de usuarios"""
    return HttpResponse("Registro de usuarios")

def aboutme(request):
    """ Registro de usuario"""
    return HttpResponse("Rey")

def greeting(request,nombre):
    """ Registro de usuarios"""
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")

def destination(request, titulo,nombre, cargo):
    """Registro de usuarios"""
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es {cargo}")

def base_triangulo(request, base,altura):
    """Registro de usuarios"""
    return HttpResponse(f"El área de un triangulo es: {(base*altura)/2}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)
def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Reymonth",
        "Apellido": "Arias"
    }
    return render(request, "leads/leads-like.html", contexto)




def project_list(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form, "modo": "editar"})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect("tasks:project-list")
    else:
        form =  ProjectForm()

    return render(request, "projects/project_form.html", {"form": form, "modo": "crear"})