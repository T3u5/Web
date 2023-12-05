from django.shortcuts import render, redirect
from .models import *
from .forms import *




# Página inicial
def index(request):
    context = {
        'title': 'Página inicial',
    }
    return render(request, 'index.html', context)

# Funções inserir
def cadastro_pessoa(request):
    pessoa_form = PessoaForm()
    pessoa_fisica_form = PessoaFisicaForm()
    pessoa_juridica_form = PessoaJuridicaForm()

    if request.method == 'POST':
        tipo_pessoa = request.POST.get('tipo_pessoa')
        if tipo_pessoa == 'fisica':
            pessoa_form = PessoaForm(request.POST)
            pessoa_fisica_form = PessoaFisicaForm(request.POST)
            if pessoa_form.is_valid() and pessoa_fisica_form.is_valid():
                pessoa = pessoa_form.save()
                pessoa_fisica = pessoa_fisica_form.save(commit=False)
                pessoa_fisica.pessoa = pessoa
                pessoa_fisica.save()
               

        elif tipo_pessoa == 'juridica':
            pessoa_form = PessoaForm(request.POST)
            pessoa_juridica_form = PessoaJuridicaForm(request.POST)
            if pessoa_form.is_valid() and pessoa_juridica_form.is_valid():
                pessoa = pessoa_form.save()
                pessoa_juridica = pessoa_juridica_form.save(commit=False)
                pessoa_juridica.pessoa = pessoa
                pessoa_juridica.save()
                

    return render(request,'cadastro_pessoa.html',{
        'pessoa_form': pessoa_form,
        'pessoa_fisica_form': pessoa_fisica_form,
        'pessoa_juridica_form': pessoa_juridica_form,

    })


# função listar
def listar_pessoa(request):
    pessoa = Pessoa.objects.all()
    pessoas_fisicas = PessoaFisica.objects.all()
    pessoas_juridicas = PessoaJuridica.objects.all()

    context = {
        'pessoas': pessoa,
        'pessoas_fisicas': pessoas_fisicas,
        'pessoas_juridicas': pessoas_juridicas,
    }
    return render(request, 'listar_pessoa.html', context)

# função listar por id
# função editar
# função remover

