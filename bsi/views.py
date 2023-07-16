from django.shortcuts import render
from datetime import date
from django.shortcuts import redirect
from django.contrib import messages
from .models import Aluno
from .forms import AlunoModelForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def alunos2(request):
    """ View da tabelas contendo os Alunos Cadastrados.
    """
    if str(request.user) != 'AnonymousUser':
        alunos = Aluno.objects.all()

        for aluno in alunos:
            idade = (date.today() - aluno.data_nascimento).days // 365
            aluno.idade = idade

        form = AlunoModelForm()

        context = {
            'alunos': alunos,
            'form': form,
            'form_url': 'cadastrar_aluno/'
        }

        return render(request, 'alunos_cadastrados.html', context)
    else: 
        return redirect('index')

def cadastrar_aluno(request):
    """ View do formulario de cadastro de aluno.
    """

    form = AlunoModelForm(request.POST, request.FILES)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Aluno cadastrado.')
        else:
            messages.error(request, 'Erro ao cadastrar o aluno. Tente novamente.')

    return redirect('/alunos')

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