from django.db import models
from usuarios.models import Usuario, Categoria


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

    status = models.IntegerChoices(
        choices=STATUS_CHOICES,
        default=1,
    )


    class Meta:
        verbose_name = ('Salario')
        verbose_name_plural = ('Salario')
        ordering = ('usuario')

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


    def escolhas_categoria(self):
        # Retorna um dicionário que limita as escolhas do campo carteira
        if self.usuario:
            return {'usuario': self.usuario}
        else:
            return {}
        
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=escolhas_categoria,
        verbose_name='Categoria',
    )

    valor = CampoMonetario(verbose_name="Valor Planejado")

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categoria')
        ordering = ('salario', 'categoria')

    def __str__(self):
        return f'{self.usuario} - {self.categoria}'