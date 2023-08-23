from django.db import models

# Create your models here.
class Aplicação(models.Model):

    class Meta:
        verbose_name_plural = "Aplicações"

    nome = models.CharField(max_length=50)
    
    
    STATUS_OPTIONS = [
        ("Fora do ar","Fora do ar"),
        ("Em funcionamento", "Em funcionamento"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS)

    list_filter = ["status"]

    def __str__(self):
        return self.nome

