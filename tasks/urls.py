from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('signup/',views.signup, name='signup'),
    path('tasks/',views.tasks, name='tasks'),
    path('cerrar_sesion/',views.cerrar_sesion, name='cerrar_sesion'),
    path('inicio_sesion/',views.inicio_sesion, name='inicio_sesion'),
    path('tasks/create/',views.create_task, name='tasks_create'),
    path('tasks/<int:task_id>/',views.task_detail, name='tasks_detail'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='task_complete'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='task_delete'),
    path('tasks/completed', views.task_completed, name='tasks_completed'),
     # NUEVA RUTA PARA ADMINISTRADORES
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
