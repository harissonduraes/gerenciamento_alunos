from django.urls import path
#from .views import index
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
path('alunos/', views.alunos_cadastrados, name='alunos_cadastrados')

]