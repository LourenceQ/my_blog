from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'semanal'
    priority = 0.9

    def items(self):
        return Post.publicado.all()

    def lastmod(self, obj):
        return obj.atualizado
