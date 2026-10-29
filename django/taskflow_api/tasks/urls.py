from django.urls import path
from . import views


app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [ 
    path("", views.home, name="home"),  
    path("register", views.register, name="register"), 
    path("aboutme", views.aboutme, name="Rey"), 
    path("saludo/<str:nombre>/",
         views.greeting, name="saludo"),
    path("destinatario/<str:titulo>/<str:nombre>/",
         views.destination, name="destinatario"),
    path("base-triangulo/<int:base>/<int:altura>/",
         views.base_triangulo, name="base-triangulo"),
    path("my-first-template",
         views.my_first_template,
         name="my-first-template"),
     path("leads-like",
          views.leads_like,
          name="leads-like"),
     
     path("projects", 
          views.project_list, name="project-list"),

     path("tasks/new/",
           views.task_create, name="task_create"),
     path("tasks/<int:pk>/edit/", views.task_edit, name="task_edit"),

     path("projects/new/",
                views.project_create, name="task_create"),



]