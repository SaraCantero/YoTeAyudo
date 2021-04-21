from django.contrib import admin
from nucleo.models import Cliente, Especialista, cita, mensaje

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'direccion' , 'biografia')
    fields = [('dni' , 'idUsuario') , ('apellidos', 'nombre' ),'fechaNacimiento', 'foto' , 'direccion' , 'biografia' ]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos')
  


@admin.register(cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'idCliente', 'idEspecialista', 'informe','realizada')
    list_filter = ('realizada' , 'fecha')
    




@admin.register(mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('idEmisor', 'idReceptor', 'fecha','asunto','leido')
    

