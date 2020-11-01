from django.utils.safestring import mark_safe
import markdown
from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.publicado.count()

@register.inclusion_tag('blog_app/post/ultimos_posts.html')
def mostrar_ultimos_posts(count=5):
    ultimos_posts = Post.publicado.order_by('-publicar')[:count]
    return {'ultimos_posts': ultimos_posts}

@register.simple_tag
def get_postagens_mais_comentadas(count=5):
    return Post.publicado.annotate(
                total_commentarios=Count('comentarios')
                ).order_by('-total_commentarios')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
