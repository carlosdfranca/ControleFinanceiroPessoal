from django.db import models
from usuarios.models import Usuario, Carteira, Categorias
# Create your models here.
class Movimentacoes(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuario',
        related_name = 'movimentacao_usuario',
    )

    carteira = models.ForeignKey(
        Carteira,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Carteira',
        related_name = 'movimentacao_carteira',
    )

    categoria = models.ForeignKey(
        Categorias,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Categoria',
        related_name = 'movimentacao_categoria',
    )

    TIPO_CHOICES = [
        (1, 'Receita'),
        (2, 'Despesa'),
    ]

    descricao = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    class Meta:
        verbose_name = ('Movimentações')
        verbose_name_plural = ('Movimentações')
        ordering = ('usuario', 'carteira', 'categoria', 'tipo')

    def __str__(self):
        return f'{self.tipo} / {self.data} - {self.valor}'