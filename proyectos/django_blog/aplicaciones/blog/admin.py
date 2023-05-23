from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResorce(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResorce(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre',]
    list_display=('nombre', 'estado', 'fecha_creacion',)
    resource_class = CategoriaResorce
    
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombres',  'apellidos', 'correo']
    list_display=('nombres','apellidos','correo', 'estado', 'fecha_creacion',)
    resource_class = AutorResorce
    

    
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)