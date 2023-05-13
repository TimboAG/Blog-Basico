from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre de la categoría", max_length=200, blank=False, null=False)
    estado= models.BooleanField("Categoría activada/Categoría Desactivada", default=True)
    fecha_creacion=models.DateField("Fecha de creación", auto_now=False, auto_now_add=True )
    
    class Meta:
        verbose_name='Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self) :
        return self.nombre
    
class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    nombres = models.CharField("Nombres del autor", max_length=200, blank=False, null=False)
    apellidos = models.CharField("Apellidos del autor", max_length=200, blank=False, null=False)
    facebook = models.URLField("Facebook", max_length=200, blank=True, null=True)
    twitter = models.URLField("Twitter", max_length=200, blank=True, null=True)
    instagram = models.URLField("Instagram", max_length=200, blank=True, null=True)
    web = models.URLField("Web", max_length=200, blank=True, null=True)
    correo = models.EmailField("Correo electrónico", max_length=254, blank=False, null=False)
    estado= models.BooleanField("Autor activo/Autor no activo", default=True)
    fecha_creacion=models.DateField("Fecha de creación", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name= "Autor"
        verbose_name_plural = "Autores"
        
    def __str__(self) :
        return self.nombres + " " + self.apellidos
    
class Post(models.Model):
    id= models.AutoField(primary_key=True)
    titulo=models.CharField("Titulo", max_length=100, blank=False,null=False)
    slug=models.CharField("Slug", max_length=100, blank=False, null=False)
    descripcion= models.CharField("Descripción", max_length=100, blank=False, null=False)
    contenido= RichTextField()
    imagen = models.URLField("Imagen", max_length=200, blank=False, null=False)
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activo= models.BooleanField("Publicado/No publicado", default=True)
    fecha_creacion= models.DateField("Fecha de creación", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name= "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self) :
        return self.titulo 