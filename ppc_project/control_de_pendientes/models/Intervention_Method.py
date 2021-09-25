
from django.db import models

class Intervention_Method(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name