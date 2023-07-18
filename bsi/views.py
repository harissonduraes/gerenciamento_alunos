from django.shortcuts import render
from datetime import date
from django.shortcuts import redirect
from django.contrib import messages
from .models import Aluno
from .forms import AlunoModelForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def cadastro_aluno(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = AlunoModelForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Aluno cadastrado com sucesso')
                form = AlunoModelForm()
            else: messages.error(request, 'Erro ao cadastrar Aluno')
        else: form = AlunoModelForm()

        context = {
            'form': form
        }
        return render(request,'cadastro_aluno.html', context)
    else:
        return redirect('index')

def alunos_cadastrados(request):
    context = {
        'alunos': Aluno.objects.all()
    }
    return render(request,'alunos_cadastrados.html',context)