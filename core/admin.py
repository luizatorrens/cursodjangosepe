from django.contrib import admin

from .models import Categoria, TipoAtuação, Pais, Produtora, Membro, Filme

admin.site.register(Categoria)
admin.site.register(TipoAtuação)
admin.site.register(Pais)
admin.site.register(Produtora)
admin.site.register(Membro)
admin.site.register(Filme)