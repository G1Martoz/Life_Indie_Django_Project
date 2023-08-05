from typing import Any, Dict, Tuple
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# Categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)


def str(self):
    return self.nombre


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='posts', default=None)
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, default='Sin Categoria')  # type: ignore
    imagen = models.ImageField(
        null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def str(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):

        self.imagen.delete()

        super().delete(using=using, keep_parents=keep_parents)
