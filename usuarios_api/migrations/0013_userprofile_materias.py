# Generated by Django 5.1 on 2024-10-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_api', '0012_userprofile_created_by_userprofile_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='materias',
            field=models.ManyToManyField(blank=True, to='usuarios_api.materias'),
        ),
    ]