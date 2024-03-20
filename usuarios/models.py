from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage.models import StdImageField
from colorfield.fields import ColorField
from bancos.models import DadosInstitucionais

import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'usuarios/{uuid.uuid4()}.{ext}'
    return filename


STATUS_CHOICES = [
    (1, 'Ativo'),
    (2, 'Inativo'),
]

# Create your models here.
class Usuario(AbstractUser):
    imagem_perfil = StdImageField(
        upload_to='get_file_path',
        variations={
            'medium': {
                'width': 300,
                'height': 300,
                'crop': True,
            }
        },
        delete_orphans=True,  # Remove variações antigas quando a imagem é alterada
        default='usuarios/default.png'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        db_table = 'usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Carteira(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
        related_name = 'usuario',
    )

    saldo_inicial = models.DecimalField(
        max_digits=10,
        decimal_places=2,  
        default=0,
        verbose_name='Saldo Inicial'

    )

    instituicao = models.ForeignKey(
        DadosInstitucionais,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'categoria': 2},
        verbose_name='Instituição Financeira',
        related_name = 'instituicao_financeira',
    )

    descricao = models.CharField(max_length=255)

    tipo_conta = models.ForeignKey(
        DadosInstitucionais,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'categoria': 1},
        verbose_name='Tipo da conta',
    )

    cor = ColorField(default='#CC99FF')

    status = models.IntegerField(
        choices=STATUS_CHOICES,
    )

    class Meta:
        verbose_name = ('Carteira')
        verbose_name_plural = ('Carteira')
        ordering = ('usuario', 'instituicao', 'tipo_conta')

    def __str__(self):
        return f'{self.banco}'
    


class Categorias(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuario',
        related_name = 'categoria_usuario',
    )


    TIPO_CHOICES = [
        (1, 'Receita'),
        (2, 'Despesa'),
    ]

    tipo_transacao = models.IntegerField(
        choices=TIPO_CHOICES,
    )

    nome = models.CharField(
        max_length = 50
    )

    cor = ColorField(default='#FF0000')


    class Meta:
        verbose_name = ('Categorias')
        verbose_name_plural = ('Categorias')
        ordering = ('usuario', 'nome')

    def __str__(self):
        return self.nome