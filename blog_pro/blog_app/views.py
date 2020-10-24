from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def lista_post(request): # ESSA VIEW PEGA A REQUEST COMO ÚNICO PARÂMETRO. PARÂMETRO REQUERIDO POR TODAS AS VIEWS
    posts = Post.publicado.all() # NESSA VIEW, É RETIRADA TODOS OS POSTS COM STATUS DE publicado USANDO O MANAGER publicado que foi criado.
    return render(request, # render É UM ATALHO FORNECIDO POR DJANGO PARA RENDERIZAR A LISTA DE POSTS NO DADO TEMPLATE.
                  'blog/post/lista.html' # ESSA FUNÇÃO PEGA O OBJETO REQURIDO, O CAMINHO DO TEMPLATE E AS VARIÁVEIS DO CONTEXTO PARA RENDERIZAR O DADO TEMPLATE
                  {'posts':posts}) # rETORNANDO UM OBJETO HttpResponse COM O TEXTO RENDERIZADO(CODIGO HTML)


# VIEW PARA DEMONSTRAR UM ÚNICO POST.
def detalhe_post(request, ano, mes, dia, post):
    post = get_object_or_404(Post, slug= post,
                                   status='publicado',
                                   publicar__ano=ano,
                                   publicar__mes=mes,
                                   publicar__dia=dia)
    return render(request,
                  'blog/post/detalhe.html',
                  {'post':post})
