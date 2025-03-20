from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()  
    imagens = models.ManyToManyField('ImagemProduto', related_name='produtos', blank=True)
    exibir_na_home = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class ImagemProduto(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return f"Imagem do {self.produto.nome}"

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    nome_cliente = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    numero_cartao = models.CharField(max_length=16)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total = self.produto.preco * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} para {self.nome_cliente}"

class CustomUser(AbstractUser):
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True) 
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_users', blank=True
    )
