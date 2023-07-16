from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
# Create your models here.

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    curso = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()
    #foto_perfil = StdImageField('Foto do Aluno', upload_to='alunos', variations={'thumb': (124, 124)})
    foto_perfil = models.URLField('Url da imagem')

    def __str__(self) -> str:
        return str(self.nome)

    
def aluno_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
signals.pre_save.connect(aluno_pre_save, sender=Aluno)