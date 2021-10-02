
from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Pending(models.Model):
    area                = models.ForeignKey('Area', on_delete=models.CASCADE , verbose_name="Área")
    system              = models.ForeignKey('System', on_delete=models.CASCADE , verbose_name="Sistema")
    machine             = models.CharField(max_length=50 , verbose_name="Equipo / Instrumento")
    description         = models.TextField(max_length=200 , verbose_name="Descripción")
    intervention_method = models.ForeignKey('Intervention_Method', on_delete=models.CASCADE , verbose_name="Método de Intervención")
    criticality         = models.ForeignKey('Criticality', on_delete=models.CASCADE , verbose_name="Criticidad")
    specialty           = models.ForeignKey('Specialty', on_delete=models.CASCADE , verbose_name="Especialidad")
    detection_date      = models.DateField(verbose_name="Fecha de detección")
    user                = models.ForeignKey(User, on_delete=models.CASCADE , default=User , verbose_name="Reportado por" , null=True)
    registration_date   = models.DateField(default=timezone.now , editable = False , verbose_name="Fecha de registro")
    notice_number       = models.CharField(max_length=8, null=True, blank=True , verbose_name="Número de aviso")
    state               = models.ForeignKey('State', on_delete=models.CASCADE , verbose_name="Estado")
    observations        = models.TextField(max_length=200 , null=True, blank=True , verbose_name="Observaciones")


    def __str__(self):
        return f'{self.area} -*-{self.system} -*- {self.description} -*- {self.user}'
    def get_absolute_url(self):
        return ("feed")