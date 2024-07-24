from django.urls import path
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import index, contato, blogs, produtos, produto_single

urlpatterns = [
    path('', index),
    path('index', index, name='index'),
    path('contato', contato, name='contato'),
    path('blogs', blogs, name='blogs'),
    path('produtos', produtos, name='produtos'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>/', produto_single, name='produto_single'),
]


# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato