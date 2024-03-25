from django.db import models
from usuarios.models import Usuario, CartaoCredito, Carteira, Categoria

def limitar_escolhas_carteira(instance):
    return instance.limitar_escolhas()


def limitar_escolhas_categoria(instance):
    return instance.limitar_escolhas()

STATUS_CHOICES = [
    (0, 'Inativo'),
    (1, 'Ativo'),
]

class CampoMonetario(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_digits', 10)
        kwargs.setdefault('decimal_places', 2)
        kwargs.setdefault('verbose_name', 'Valor')
        super().__init__(*args, **kwargs)


# Create your models here.
class Movimentacoes(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
        related_name = 'movimentacao_usuario',
    )

    TIPO_MOVIMENTACAO_CHOICES = [
        (1, "Receita"),
        (2, "Despesa"),
    ]

    tipo_movimentacao = models.IntegerField(
        choices=TIPO_MOVIMENTACAO_CHOICES
    )

    descricao = models.CharField(max_length=(100))

    valor = CampoMonetario(verbose_name="Valor")

    data = models.DateField()
        
    carteira = models.ForeignKey(
        Carteira,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=limitar_escolhas_carteira,
        verbose_name='Carteira',
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=limitar_escolhas_categoria,
        verbose_name='Categoria',
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
    )

    class Meta:
        verbose_name = ('Movimentações')
        verbose_name_plural = ('Movimentações')
        ordering = ('usuario', 'carteira', 'categoria', 'data', 'tipo_movimentacao' , 'valor')

    def __str__(self):
        return f'{self.usuario}'


class credito(models.Model):
    def escolhas_usuario(self):
        # Retorna um dicionário que limita as escolhas do campo carteira
        if self.usuario:
            return {'usuario': self.usuario}
        else:
            return {}
        
    cartao = models.ForeignKey(
        CartaoCredito,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=escolhas_usuario,
        verbose_name='Cartão de Crédito',
    )

    valor = CampoMonetario()

    descricao = models.CharField(max_length=100)

    data = models.DateField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=escolhas_usuario,
        verbose_name='Categoria',
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
    )

    class Meta:
        verbose_name = ('Crédito')
        verbose_name_plural = ('Crédito')
        ordering = ('cartao', 'data', 'categoria', 'valor')

    def __str__(self):
        return f'{self.cartao}'