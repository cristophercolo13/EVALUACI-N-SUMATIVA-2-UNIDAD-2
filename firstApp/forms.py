from django import forms
from firstApp.models import Equipo

 
class FormEquipo(forms.ModelForm):
   class Meta:
       model = Equipo
       fields = ("__all__")
    
n_equipo = forms.CharField(required=True)
n_entrenador = forms.CharField(required=True) 
n_estadio =forms.CharField()
titulos = forms.CharField()
n_ciudad = forms.CharField()
p_origen = forms.CharField()


