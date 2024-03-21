from django.db import models
from stdimage.models import StdImageField
from colorfield.fields import ColorField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'dados_institucionais/{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class DadosInstitucionais(models.Model):
    nome = models.CharField(max_length=100)

    logo = StdImageField(
        upload_to=get_file_path,
        variations={
            'medium': {
                'width': 300,
                'height': 300,
                'crop': True,
            }
        },
        delete_orphans=True,  # Remove variações antigas quando a imagem é alterada
        default='dados_institucionais/default.png'
    )

    CATEGORIA_CHOICES = [
        (1, 'Tipo de conta'),
        (2, 'Instituição Financeita'),
        (3, 'Bandeira do cartão'),
    ]

    categoria = models.IntegerField(
        choices=CATEGORIA_CHOICES,
    )

    class Meta:
        verbose_name = ('Dados Institucionais')
        verbose_name_plural = ('Dados Institucionais')
        ordering = ('categoria', 'nome')

    def __str__(self):
        return f'{self.nome} - {self.categoria}'