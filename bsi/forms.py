from django import forms
from django.core.mail.message import EmailMessage
from django.conf import settings
from .models import Aluno

class AlunoModelForm(forms.ModelForm):
    class Meta:
            model = Aluno
            fields = ['nome', 'foto_perfil', 'cpf', 'rg', 'curso', 'data_nascimento', 'data_ingresso']

    data_nascimento = forms.DateField(label="Data de Nascimento",
                                      input_formats=settings.DATE_INPUT_FORMATS,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'type': 'date'})
                                      )

    data_ingresso = forms.DateField(label="Data de Ingresso",
                                    input_formats=settings.DATE_INPUT_FORMATS,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'type': 'date'})
                                    )
