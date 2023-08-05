from django.db import models
from django.utils import timezone
from django.conf import settings

class Comentario(models.Model):
    posts = models.ForeignKey('posts.Posts', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
