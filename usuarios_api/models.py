from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django import forms
from django.conf import settings

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
      
        if user.is_teacher:
            Profesor.objects.create(user=user)
        elif user.is_student:
            Estudiante.objects.create(user=user)
        
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

    
class NivelEscolar(models.Model): 
    nombre = models.CharField(max_length=50)   
    
class Materias(models.Model): #matematicas, ingles, etc
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(default='')
    nivel_escolar = models.ForeignKey(NivelEscolar, on_delete=models.CASCADE )

    
class Asignacion(models.Model):
    #nombre = models.ForeignKey(Materias, on_delete=models.CASCADE)
    nombre = models.TextField(Materias)
    description = models.TextField()
    fechaLimite = models.DateField()
    
class Tarea(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # archivo =  donde se guardaran los datos que envie el estudiane
    archivo =  models.FileField(upload_to= 'tareas/')
    
class Profesor(models.Model):
    # el user se regiere al usuario que es profesor 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profesor_profile')
    materias = models.ManyToManyField(Materias, related_name='profesor_materias')
    
class Estudiante(models.Model):
    #se refiere al usuario que es un profesor
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='estudiante_profile')
    materias = models.ManyToManyField(Materias, related_name='estudiante_materias')  
    
class TareaForm(forms.ModelForm):
    class Meta: 
        model = Tarea
        fields = ('archivo', 'asignacion')
    
    
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique= True)
    #password = models.CharField(max_length=100)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_users', default=1)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='updated_users', default=1)
    materias = models.ManyToManyField(Materias, blank=True)
    profesor = models.OneToOneField(Profesor, on_delete=models.CASCADE, null=True, blank=True)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    
    def is_student_or_teacher(self):
        return self.is_student or self.is_teacher
    
    

