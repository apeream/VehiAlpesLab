from django.contrib import admin

from .models import Vendedor, Perfil, PerfilVendedor, Prospecto

# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Perfil)
admin.site.register(PerfilVendedor)
admin.site.register(Prospecto)