from django.urls import path
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import index, contato, mercado, produto

urlpatterns = [
    path('', index),
    path('index', index),
    path('contato', contato),
    path('mercado', mercado),
    path('produtos', produto)
]

# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato