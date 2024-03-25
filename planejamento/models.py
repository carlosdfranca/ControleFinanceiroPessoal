from django.db import models
from usuarios.models import Usuario, Categoria


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
class Salario(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
        related_name = 'salario_usuario',
    )

    salario = CampoMonetario(verbose_name="Salário")

    economia = models.DecimalField(
        max_digits=5,
        decimal_places=2,  
        default=0,
        verbose_name='Porcentagem da Economia'     
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
    )


    class Meta:
        verbose_name = ('Salario')
        verbose_name_plural = ('Salario')
        ordering = ('usuario', )

    def __str__(self):
        return f'{self.usuario}'
    


class Categoria(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
        related_name = 'categoria_usuario',
    )

    salario = models.ForeignKey(
        Salario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Salário',
        related_name = 'categoria_salario',
    )

        
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Categoria',
    )

    valor = CampoMonetario(verbose_name="Valor Planejado")

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categoria')
        ordering = ('salario', 'categoria')

    def __str__(self):
        return f'{self.usuario} - {self.categoria}'