from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)


class PessoaFisica(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    data_nascimento = models.DateField(blank=True, null=True)
    rg = models.CharField(max_length=12, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    
    
class PessoaJuridica(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE) 
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    nome_empresa = models.CharField(max_length=255, null=True, blank=True)

    