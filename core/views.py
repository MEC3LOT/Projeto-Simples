from django.shortcuts import render, get_object_or_404
from core.models import Products, Blog, Cars

# Create your views here.

def index (request):
    context = {
        'courses' : ['Programação de Computadores no Senac   Guaratinguetá'],
        'languages' : ['Python','Java','C++', 'JavaScript' ],
        'books' : ['Livro 1','Livro 2','Livro 3', 'Livro 4' ],
        'title': 'Web Django',
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
    context ={
        'title': 'Contato Site'
    }
    return render(request, 'contato.html',)


def blogs(request):
    blog = Blog.objects.all()

    data = {
        'blog': blog,
        'title': 'Blog Django'
    }
    return render(request, 'blogs.html', data)


#Página single do blog com slug, url amigável
def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})

    return render(request, 'blogs.html', context)

def produtos(request):
    product = Products.objects.all() # Products.objects.all() -> Usado para recuperar todos os objetos de um modelo (Dados de uma tabela).

    data = {
        'product': product,
    }
    return render(request, 'produtos.html', data)



def produto_single(request, id):
    products = get_object_or_404(Products, id=id) # get_object_or_404(Products, id=id) -> Usado para recuperar um único objeto com base em um critério específico, como um ID único.
    return render(request, 'produto_single.html', {'products': products})  



def carros(request):
    cars = Cars.objects.all() # Products.objects.all() -> Usado para recuperar todos os objetos de um modelo (Dados de uma tabela).

    data = {
        'cars': cars,
    }
    return render(request, 'carros.html', data)