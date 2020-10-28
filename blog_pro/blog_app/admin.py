from django.contrib import admin
from .models import Post, Comentarios

# Register your models here.

# TELLING DJANGO THAT THE MODEL IS REGISTERED IN THE SITE USING
# AS CUSTOM CLASS THAT INHERITS FROM Model.Admin
@admin.register(Post) # THIS DECORATOR PERFORMS THE SAME FUNCTION AS THE admin.site.register() function
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','slug','autor','publicar','status')
# THE list_display attribute allows to set the fields og the model
# that I want to display o the administration object list page.
    list_filter = ('status','criado','publicar','autor')
    search_fields = ('titulo','body')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicar'
    ordering = ('status','publicar')

@admin.register(Comentarios)
class ComentarAdmin(admin.ModelAdmin):
    exibir_lista = ('nome', 'email', 'post', 'criado', 'ativo')
    filtro_lista = ('ativo', 'criado', 'atualizado')
    campo_pesquisa = ('nome', 'email', 'body')
