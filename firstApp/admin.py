from django.contrib import admin
from firstApp.models import Equipo

# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = ['n_equipo','n_entrenador','n_estadio','titulos','n_ciudad','p_origen']
  
admin.site.register(Equipo,EquipoAdmin)