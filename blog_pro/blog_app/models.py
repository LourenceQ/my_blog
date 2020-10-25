from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class AdminPub(models.Manager):
    def get_queryset(self): # ESSE MÉTODO DE UM MANAGER RETORNA A QuerySet QUE VAI SER EXECUTADA
        return super(AdminPub,
                     self).get_queryset()\
                          .filter(status='publicado') # SOBREESCREVE O MÉTODO ACIMA PARA INCLUIR O MANAGER COSTOMIZADO

class Post(models.Model):

    ESCOLHA_STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250) # ESSE CAMPO É PARA O TÍTULO DO POST
    slug = models.SlugField(max_length=250,   # ESSE CAMPO É PARA SER USADO NAS URLS.
                            unique_for_date='publicar') # SLUG É UM RÓTULO QUE CONTEM APENAS LETRAS, NÚMEROS ETC...
    autor = models.ForeignKey(User, # ESSE CAMPO DENIFE  RELAÇÃO many-to-one.
                            on_delete=models.CASCADE, # OU SEJA: CADA POST É ESCRITO POR APENAS UM USUÁRIO
                            related_name='blog_posts') # E UM USUÁRIO PODE ESCREVER QUALQUER NUMERO DE POSTS.

    body = models.TextField() # ESSE É  O CORPO DO POST. É UM CAMPO DE TEXT QUE É ENVIADO PARA A BASE DE DADOS SQL
    publicar = models.DateTimeField(default=timezone.now) # DateTimeField INDICA QUANDO FOI O POST
    criado = models.DateTimeField(auto_now_add=True) # INDICA QUANDO O POST FOI CRIADO
    atualizado = models.DateTimeField(auto_now=True) # INDICA A ULTIMA VEZ QUE O POST FOI ATUALIZADO
    status = models.CharField(max_length=10, # MOSTRA O STATUS DO POST
                                choices=ESCOLHA_STATUS,
                                default='rascunho')
    objetos = models.Manager() # MANAGER PADRÃO
    publicado = AdminPub() # MANAGER PERSONALIZADO

    class Meta: # ESSA CLASSE CONTÉM METADATA. DJANGO ORDENA OS RESULTADOS
        ordering = ('-publicar',) # PELO CAMPO DE PUBLICAÇÃO EM ORDEM DECRESCENTE
                                      # QUANDO CONSULTA A BASE DE DADOS
    def get_absolute_url(self):
        return reverse('blog_app:detalhe_post',
                        args=[self.publicar.year,
                              self.publicar.month,
                              self.publicar.day, self.slug])

    def __str__(self): # METODO PADRÃO PARA LEITURA DO OBJETO
        return self.titulo
