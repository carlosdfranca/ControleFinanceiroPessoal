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
    (0, 'Inativo'),
    (1, 'Ativo'),
]

class CampoMonetario(models.Model):
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,  
        default=0,
        verbose_name='valor'     
    )

    class Meta:
        abstract = True




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
        related_name = 'carteira_usuario',
    )

    saldo_inicial = CampoMonetario(verbose_name='Saldo Inicial')

    instituicao = models.ForeignKey(
        DadosInstitucionais,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'categoria': 2},
        verbose_name='Instituição Financeira',
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
        defalt=1,
    )

    class Meta:
        verbose_name = ('Carteiras')
        verbose_name_plural = ('Carteiras')
        ordering = ('usuario', 'instituicao', 'tipo_conta')

    def __str__(self):
        return f'{self.banco}'
    


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
    )

    cor = ColorField(default='#FF0000')

    TIPO_TRANSACAO_CHOICES = [
        (1, 'Receita'),
        (2, 'Despesa'),
    ]

    tipo_transacao = models.IntegerField(
        choices=TIPO_TRANSACAO_CHOICES,
    )

    status = models.IntegerChoices(
        choices=STATUS_CHOICES,
        default=1,
    )


    class Meta:
        verbose_name = ('Categorias')
        verbose_name_plural = ('Categorias')
        ordering = ('usuario', 'nome')

    def __str__(self):
        return f'{self.nome}'
    


class CartaoCredito(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
        related_name = 'cartao_usuario',
    )

    descricao = models.CharField(max_length=50)

    limite = CampoMonetario(verbose_name='Limite')

    bandeira = models.ForeignKey(
        DadosInstitucionais,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'categoria': 3},
        verbose_name='Bandeira do cartão',
    )

    def escolhas_carteira(self):
        # Retorna um dicionário que limita as escolhas do campo carteira
        if self.usuario:
            return {'usuario': self.usuario}
        else:
            return {}

    carteira = models.ForeignKey(
        Carteira,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=escolhas_carteira,
        verbose_name='Bandeira do cartão',
    )

    DIAS_NO_MES = [(i, str(i)) for i in range(1, 32)]

    dia_fechamento = models.IntegerField(
        choices=DIAS_NO_MES,
        verbose_name='Dia do Fechamento'
    )

    dia_vencimento = models.IntegerField(
        choices=DIAS_NO_MES,
        verbose_name='Dia do Vencimento'
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        defalt=1,
    )