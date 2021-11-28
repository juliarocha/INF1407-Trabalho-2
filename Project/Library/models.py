from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField("Name", max_length=80)
    email = models.CharField("Email", max_length=80)
    password = models.CharField("Password", max_length=20)


class Livros(models.Model):
    name = models.CharField('Título', max_length=100)
    author = models.CharField('Autor(a)', max_length=200)
    publishingHouse = models.CharField('Editora', max_length=200)
    readStatus = models.BooleanField('Status de Lido', blank='False')
    review = models.IntegerField('Review', help_text='Entre a nota - 0 a 5 (Para não lidos, entre 0)')
    year = models.IntegerField('Ano Lido/Adicionado')


    def __str__(self):
        return self.nome

class Request(models.Model):
    name = models.CharField('Name', max_length=100)
    author = models.CharField('Author', max_length=200)
    base_url = models.CharField('URL', max_length=200)

    def __str__(self):
        return self.nome