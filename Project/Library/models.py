from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField("Name", max_length=80)
    email = models.CharField("Email", max_length=80)
    password = models.CharField("Password", max_length=20)


class Request(models.Model):
    name = models.CharField('Name', max_length=100)
    author = models.CharField('Author', max_length=200)
    base_url = models.CharField('URL', max_length=200)

    def __str__(self):
        return self.nome