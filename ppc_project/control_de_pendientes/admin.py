from django.contrib import admin

from control_de_pendientes.models.Area import Area
from control_de_pendientes.models.System import System
from control_de_pendientes.models.Intervention_Method import Intervention_Method
from control_de_pendientes.models.Pending import Pending
from control_de_pendientes.models.Criticality import Criticality
from control_de_pendientes.models.Specialty import Specialty
from control_de_pendientes.models.State import State

# Register your models here.

admin.site.register(Area)
admin.site.register(System)
admin.site.register(Intervention_Method)
admin.site.register(Pending)
admin.site.register(Criticality)
admin.site.register(Specialty)
admin.site.register(State)


