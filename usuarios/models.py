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
    # rpps_id = models.ForeignKey(RPPS, null=True, blank=True, default=0, on_delete=models.SET_DEFAULT)
    # data_criacao = models.DateTimeField(auto_now_add=True)
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


    class Meta:
        ordering = ('first_name', 'last_name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'