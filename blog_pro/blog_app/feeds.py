from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class UltimosPostsFeed(Feed):
    titulo = "Meu Blog"
    link = reverse_lazy('blog_app:lista_post')
    description = 'Novos posts do meu blog.'


    def items(self):
        return Post.publicado.all() [:5]

    def item_titulo(self, item):
        return item.titulo

    def item_description(self, item):
        return truncatewords(item.body, 30)
