from django.contrib import admin
from nucleo.models import Cliente, Especialista, cita, mensaje


admin.site.register(Cliente)
admin.site.register(Especialista)
admin.site.register(cita)
admin.site.register(mensaje)

