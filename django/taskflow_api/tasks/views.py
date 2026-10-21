from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


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

def aboutme():
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
    return render(request, "tasks/my_first_template.html", contexto)
    