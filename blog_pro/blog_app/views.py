from django.shortcuts import render, get_object_or_404
from .models import Post, Comentarios
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailFormulario, ComentarioForm
from django.core.mail import send_mail
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
     # LISTA DE COMENTARIOS ATIVOS PAR O POST
    comentarios = post.comentarios.filter(ativo="True")

    novo_comentario = None

    if request.method == 'POST':
        # UM COMENTÁRIO FOI POSTADO
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            # CRIAR OBJETO DE COMENTARIO MAS NÃO SALVA NO BANCO DE DADOS AINDA
            novo_comentario = comentario_form.save(commit=False)
            # ATRIBUI O ATUAL POPST AO COMENTARIO
            novo_comentario.post = post
            # SALVA O COMENTARIO NO BANCO DE DADOS
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm
    return render(request,'blog_app/post/detalhe.html',{'post': post,
                                                        'comentarios':comentarios,
                                                        'novo_comentario': novo_comentario,
                                                        'comentario_form': comentario_form})

class PostListView(ListView):
    queryset = Post.publicado.all() #
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/post/lista.html'

def post_compartilhar(request, post_id): # DEFINE A VIEW QUE PEGA AS VARIAVEIS OBJETO DE request E post_id COMO PARÂMETROS.
    # RETIRA POSTS POR ID
    post = get_object_or_404(Post, id=post_id, status='publicado') # USA get_object_or_404 PARA RETIRAR O POST POR ID E CERTIFICA QUE O POST TEM STATUS DE PUBLICADO.
    sent = False

    if request.method =='POST':
        # FORMULÁRIO SUBMETIDO
        form = EmailFormulario(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['nome']} recomenda enquanto voce lê " \
                      f"{post.titulo}"
            message = f"Leia {post.titulo} em {post_url}\n\n" \
                      f"{cd['nome']} comentários: {cd['comentarios']}"
            send_mail(subject, message, 'lawrenceqf@gmail.com', [cd['para']])
            sent = True
            # SEND EMAIL
    else:
        form = EmailFormulario()
    return render(request,'blog_app/post/compartilhar.html',{'post':post,
                                                             'form':form,
                                                             'sent':sent})
