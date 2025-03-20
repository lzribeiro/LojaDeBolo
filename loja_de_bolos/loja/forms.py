from django import forms
from .models import Produto
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import CustomUser 
from .models import ImagemProduto
from .models import Pedido

class ProdutoForm(forms.ModelForm):
    # Adicione um campo para a imagem do produto
    imagem = forms.ImageField(label='Imagem do Produto', required=False)

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'imagem']

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['foto']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = []

class ImagemProdutoForm(forms.ModelForm):
    class Meta:
        model = ImagemProduto
        fields = ['imagem']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['quantidade', 'nome_cliente', 'cpf', 'telefone', 'numero_cartao']