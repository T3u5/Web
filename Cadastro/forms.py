from django import forms
from .models import *


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','telefone','email','endereco','bairro','cidade','estado','cep']

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ['data_nascimento','rg','cpf']

class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = ['cnpj','nome_empresa']        
    


            