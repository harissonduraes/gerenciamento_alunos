from django.urls import path
#from .views import index
from . import views

urlpatterns = [

path('', views.index, name='index'),
#path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
path('alunos/', views.alunos_cadastrados, name='alunos_cadastrados')

]