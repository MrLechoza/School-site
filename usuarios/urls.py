from django.contrib import admin
from django.urls import path, include
from usuarios_api.views import register, login




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('login/', login)
    
]