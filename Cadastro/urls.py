from django.urls import path
from .views import * 

urlpatterns = [
    
    path('', index, name='index'),
    path('cadastro_pessoa', cadastro_pessoa, name='cadastro_pessoa'),
    path('listar_pessoa', listar_pessoa, name='listar_pessoa'),
    
]



