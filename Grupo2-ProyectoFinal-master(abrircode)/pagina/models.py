from django.db import models
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria', max_length=100, blank=False, null=False)
    estado = models.BooleanField('Categoria activada/Categoria no activada', default=True)
    Fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombre del autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellido del autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    email = models.EmailField('Email',null=False, blank=False)
    estado = models.BooleanField('Activo/No Activo', default = True)
    Fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length= 255)
    url = models.SlugField(max_length = 255, unique= True)
    descripcion = models.CharField('Descripcion', max_length=100, blank=False, null=False)
    texto=models.TextField()
    imagen = models.URLField(max_length=257, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    creado = models.DateField('Fecha Creado', auto_now =False, auto_now_add = True)

# idi

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)



class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)
    comentario = models.CharField(max_length=100, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_publicacion = models.DateField('Fecha de Publicacion', auto_now =False, auto_now_add = True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
# Create your models here.
