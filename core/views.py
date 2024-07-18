from django.shortcuts import render
from core.models import Products

# Create your views here.

def index (request):
    context = {
        'courses' : 'Programação de Computadores no Senac Guaratinguetá',
        'languages' : ['Python','Java','C++', 'JavaScript' ],
        'books' : ['Livro 1','Livro 2','Livro 3', 'Livro 4' ],
        'news': [
            {
                'title' : 'Nova Versão do Django',
                'subtitle' : 'Confira as novidades da versão 2.0',
                'text' : 'lorem10'
            },
            {
                'title' : 'Pythin é de Gay',
                'subtitle' : 'Sim, pythin é de gay - - Vira Python',
                'text' : 'lorem30',
            },
            {
                'title' : 'JavaSciptito é duas vezes melhor',
                'subtitle' : 'Você está ultrapassado e precisa de uma versão atualizada',
                'text' : 'lorem50'
            },
            {
                'title' : 'JavaSciptito é duas vezes melhor',
                'subtitle' : 'Você está ultrapassado e precisa de uma versão atualizada',
                'text' : 'lorem50'
            }
        ],
        'imgs' : ['img/contato.jpg']
    }
    return render(request, 'index.html', context)


def contato (request):
    return render(request, 'contato.html')


def mercado (request):
    context = {
        'produtos': [
            {
                'nome' : 'Nova Versão do Django',
                'preço' : 'Confira as novidades da versão 2.0',
                'descrição' : 'lorem10'
            },
            {
                'nome' : 'Nova Versão do Django',
                'preço' : 'Confira as novidades da versão 2.0',
                'descrição' : 'lorem10'
            },
            {
                'nome' : 'Nova Versão do Django',
                'preço' : 'Confira as novidades da versão 2.0',
                'descrição' : 'lorem10'
            },
            {
                'nome' : 'Nova Versão do Django',
                'preço' : 'Confira as novidades da versão 2.0',
                'descrição' : 'lorem10'
            }
        ]   
    }

    return render(request, 'mercado.html', context)

def produto (request):
    product = Products.objects.all()

    data = {
        'produto': product,
    }
    return render(request, 'produtos.html', data)
