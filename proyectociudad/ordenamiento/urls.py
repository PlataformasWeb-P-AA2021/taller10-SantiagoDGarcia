from django.urls import path
from ordenamiento.views import *

urlpatterns = [
      path('', index, name='index'),
      path('parroquias/', ir_parroquias,  name='ir_parroquias'),
      path('parroquias/crear/', crear_parroquias,  name='crear_parroquias'),
      path('parroquias/editar/<int:id>', editar_parroquia,  name='editar_parroquia'),
      path('barrios/crear/', crear_barrios,  name='crear_barrios'),
      path('barrios-parroquias/', ir_barrios_parroquias,  name='ir_barrios_parroquias'),
]