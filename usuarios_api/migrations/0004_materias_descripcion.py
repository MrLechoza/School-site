# Generated by Django 5.1 on 2024-09-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_api', '0003_materias_estudiante_asignacion_profesor_tarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='materias',
            name='descripcion',
            field=models.TextField(default=''),
        ),
    ]