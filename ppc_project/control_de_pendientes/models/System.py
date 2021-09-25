
from django.db import models

class System(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey('Area', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name