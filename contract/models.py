from django.db import models

class Contact(models.Model):
    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Asunto', max_length=200)
    message = models.TextField('Mensaje')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f"{self.name} - {self.subject}"
