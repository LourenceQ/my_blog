from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailFormulario
# Create your views here.

def lista_post(request): # ESSA VIEW PEGA A REQUEST COMO ÚNICO PARÂMETRO. PARÂMETRO REQUERIDO POR TODAS AS VIEWS
    object_list = Post.publicado.all()
    paginator = Paginator(object_list, 3) # 3 POST EM CADA PÁGINA
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # SE PÁGINA Ñ FOR UM INTEIRO ENTREGA A PRIMEIRA PÁGINA
        posts = paginator.page(1)
    except EmptyPage:
        # SE PÁGINA ESTÁ FORA DO ALCANCE A ULTIMA PÁGINA É ENTREGUE
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog_app/post/lista.html',{'page':page,'posts':posts})

    #posts = Post.publicado.all() # NESSA VIEW, É RETIRADA TODOS OS POSTS COM STATUS DE publicado USANDO O MANAGER publicado que foi criado.
    #return render(request,'blog_app/post/lista.html',{'posts':posts})

 # render É UM ATALHO FORNECIDO POR DJANGO PARA RENDERIZAR A LISTA DE POSTS NO DADO TEMPLATE.
 # ESSA FUNÇÃO PEGA O OBJETO REQURIDO, O CAMINHO DO TEMPLATE E AS VARIÁVEIS DO CONTEXTO PARA RENDERIZAR O DADO TEMPLATE
 # RETORNANDO UM OBJETO HttpResponse COM O TEXTO RENDERIZADO(CODIGO HTML)

# VIEW PARA DEMONSTRAR UM ÚNICO POST.
def detalhe_post(request, year, month, day, post):
    post = get_object_or_404(Post, slug= post,
                                   status='publicado',
                                   publicar__year=year,
                                   publicar__month=month,
                                   publicar__day=day)
    return render(request,'blog_app/post/detalhe.html',{'post': post})

class PostListView(ListView):
    queryset = Post.publicado.all() #
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/post/lista.html'

def post_compartilhar(request, post_id): # DEFINE A VIEW QUE PEGA AS VARIAVEIS OBJETO DE request E post_id COMO PARÂMETROS.
    # RETIRA POSTS POR ID
    post = get_object_or_404(Post, id=post_id, status='publicado') # USA get_object_or_404 PARA RETIRAR O POST POR ID E CERTIFICA QUE O POST TEM STATUS DE PUBLICADO.
    if request.method =='POST':
        # FORMULÁRIO SUBMETIDO
        form = EmailFormulario(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # SEND EMAIL
        else:
            form = EmailFormulario()
        return render(request,'blog_app/post/compartilhar.html',{'post':post,'form':form})
