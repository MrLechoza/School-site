from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.http import HttpRequest
from .models import UserProfile, Materias
from django import forms
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password' , 'is_student', 'is_teacher', 'materias')

class UserProfileAdmin (admin.ModelAdmin):
    form = UserForm
    list_display = ('username', 'email' , 'is_student', 'is_teacher')
    list_filter = ('is_student', 'is_teacher')
    search_fields = ('username', 'email')
    actions = ['delete_selected']
    
    def delete_selected(self, request, queryset):
        queryset.delete()
        
    delete_selected.short_description = "Eliminar Seleccionados"
    
    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.is_teacher:
            self.form = UserForm
            self.form.fields['materias'] = forms.ModelMultipleChoiceField(queryset=Materias.objects.all())
        return super(UserProfileAdmin, self).get_form(request, obj, **kwargs)
                    
    def save_model(self, request, obj, form, change):
        if  'is_student' in form.cleaned_data:
            obj.is_student = form.cleaned_data['is_student']
        if  'is_teacher' in form.cleaned_data:
            obj.is_teacher = form.cleaned_data['is_teacher']
        obj.save()
        token, created = Token.objects.get_or_create(user=obj)
        obj.set_password(token.key)
        obj.save()
        return redirect('response_after_save', obj.id, token.key)
                    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'materias':
            kwargs['widget'] = forms.CheckboxSelectMultiple
        return super(UserProfileAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        

admin.site.register(UserProfile, UserProfileAdmin)