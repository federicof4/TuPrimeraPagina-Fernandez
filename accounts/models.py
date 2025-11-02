from django.db import models
from django.contrib.auth.models import AbstractUser


def user_image_path(instance, filename):
    return f'user_{instance.username}/{filename}'

class User(AbstractUser):
    user_image = models.ImageField(
        upload_to=user_image_path,
        default='default/default_user_image.png',
        blank=True,
        null=True,
        verbose_name='User Image'
    )
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=20, null=True)
    compania = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.username} - {self.email}" 