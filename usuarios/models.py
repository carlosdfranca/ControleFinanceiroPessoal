from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage.models import StdImageField

import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'profile_photo/{uuid.uuid4()}.{ext}'
    return filename


# Create your models here.
class Usuario(AbstractUser):
    imagem_perfil = StdImageField(
        upload_to='usuarios/',
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

    saldo_inicial = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        ordering = ('first_name', 'last_name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Banco(models.Model):
    nome = models.CharField(max_length=100)

    logo =  StdImageField(
        upload_to='bancos/',
        variations={
            'medium': {
                'width': 300,
                'height': 300,
                'crop': True,
            }
        },
        delete_orphans=True,  # Remove variações antigas quando a imagem é alterada
        default='bancos/default.png'
    )


    class Meta:
        verbose_name = ('Banco')
        verbose_name_plural = ('Banco')
        ordering = ('nome',)

    def __str__(self):
        return self.nome



class Carteira(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuário',
        related_name = 'usuario',
    )

    banco = models.ForeignKey(
        Banco,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Banco',
        related_name = 'banco',
    )


    class Meta:
        verbose_name = ('Carteira')
        verbose_name_plural = ('Carteira')
        ordering = ('usuario', 'banco')

    def __str__(self):
        return f'{self.usuario} - {self.banco}'