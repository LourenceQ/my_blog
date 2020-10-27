from django.urls import path
from . import views

app_name = 'blog_app' # DEFINE UMA APLICAÇÃO COM O NOME DA VARIAVEL blog_app
                      # PERMITE ORGANIZAR URL's PORAPLICAÇÃO E USAR O NOME AO SER REFERIR A ELAS

urlpatterns = [       # DEFINIDO DOIS PADRÕES DIFERENTES USANDO A FUNÇÃO path()
    #POST VIEWS
    #path('',views.lista_post, name='lista_post'), # O PRIMEIRO PADRÃO Ñ ECEBE NENHUM ARGUMETNO E MAPEADA PARA A VIEW lista_post
    path('',views.PostListView.as_view(),name='lista_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.detalhe_post,name='detalhe_post'),
    path('<int:post_id>/compartilhar/',views.post_compartilhar, name='post_compartilhar'),
]

#  O SEGUNDO PADRÃO RECEBE 4 ARGUMENTOS E É MAPEADA PARA A VIEW detalhe_post
# <> PARA CAPTURAR VALORES DA URL
# <int:ano> É UM CONERSOR DE STRING PARA INT
# EM SEGUIDA INCLUIR OS PADRÕES URLS DE blog_app PARA
# A URLS DO PROJETO
