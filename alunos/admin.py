from django.contrib import admin
from .models import *

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["nome", "email", "cpf", "data_nascimento"]