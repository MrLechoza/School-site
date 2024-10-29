from django.contrib import admin
from django.urls import path
from usuarios_api.views import register, login, user_profile,asignar_materias_estudiante, asignar_materias_profesor, obtener_materias_estudiante, obtener_materias_profesor
from usuarios_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/' , views.UserProfileView, name='usuarios_view'),
    path('usuarios/profile/image/' , views.update_profile, name='user_profile_image'),
    path('response_after_save/<int:obj_id>/<str:token_key>/', views.response_after_save, name='response_after_save'),
    path('register/', register),
    path('register/message/', views.register_message, name='register_message'),
    path('login/', login),
    path('logout/', views.logoutView, name='logout_view'),
    path('register/options/', views.register_options, name='register_options'),
    path('register/teacher-page',views.menu, name='menu'),
    path('register/teacher-page/register-student', views.register_Student_by_teacher, name='register student by teacher'),
    path('materias/agregar', views.agregar_materia, name='materias'),
    path('asignment/', views.asignacion_list, name='asinacion_list'),
    path('asignment/<int:pk>', views.asignacion_detail, name='asignacion_detail'),
    path('materias/', views.MateriaView, name='materia_view'),
    path('usuarios/profile/', user_profile, name='user_profile'),
    path('admin-asignar-materiaEs/<int:estudiante_id>/', asignar_materias_estudiante, name='asignar_materias_estudiante'),
    path('admin-asignar-materiaPr/<int:profesor_id>/', asignar_materias_profesor, name='asignar_materias_profesor'),
    path('obtener-materias-Es/', obtener_materias_estudiante, name='obtener-materias-Es'),
    path('obtener-materias-Pr/', obtener_materias_profesor, name='obtener-materias-Pr'),
]