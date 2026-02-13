from django.contrib import admin
from .models import Aluno, Professor, Curso, Disciplina

# Matricula NÃO deve ser registrada aqui conforme o enunciado.
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Disciplina)