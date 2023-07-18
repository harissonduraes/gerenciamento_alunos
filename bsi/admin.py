from django.contrib import admin
from bsi.models import Aluno

# Register your models here.

#admin.site.register(Produto)
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'data_nascimento', 'data_ingresso',)
    search_fields = ('nome', 'curso',)