from django.db import models
from django.contrib.auth.models import User

class Acortador_url(models.Model):
    url = models.URLField()
    acor_url = models.CharField(
        max_length=18, unique=True, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    profiles = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='Posts')

    def __str__(self):
        return self.acor_url

    class Meta:
        verbose_name = 'acordor_url'
        verbose_name_plural = ('acortadores_url')
        ordering = ['-created']