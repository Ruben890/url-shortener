from django.db import models


class acortador_url(models.Model):
    url = models.URLField()
    acor_url = models.CharField(max_length=18, unique=True, blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.acor_url

    class Meta:
        verbose_name='acordor_url'
        verbose_name_plural = ('acortadores_url')
        ordering = ['-created']