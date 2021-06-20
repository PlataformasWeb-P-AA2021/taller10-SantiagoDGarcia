from django.forms import ModelForm
from django import forms
from ordenamiento.models import Parroquia, BarrioCiudadela

class FormParroquia (ModelForm):
      class Meta:
            model = Parroquia
            fields = ['nombre', 'tipo']
            
class FormBarrios (ModelForm):
      class Meta:
            model = BarrioCiudadela
            fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'id_parroquia']
            
class FormBarrioDeParroquia(ModelForm): 
    def __init__(self, parroquia, *args, **kwargs):
            super(FormBarrioDeParroquia, self).__init__(*args, **kwargs)
            self.initial['id_parroquia'] = parroquia
            self.fields['id_parroquia'].widget = forms.widgets.HiddenInput()
            print(parroquia)
    
    class Meta:
            model = BarrioCiudadela
            fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'id_parroquia']
