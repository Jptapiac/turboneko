from django.db import models


class Animatronic(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to='animatronics/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


