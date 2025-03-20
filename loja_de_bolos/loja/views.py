# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Produto, Pedido
from .forms import ProdutoForm, ImagemProdutoForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomPasswordChangeForm
from .models import ImagemProduto
from .forms import PedidoForm
from django.http import HttpResponse

def home(request):
    produtos = Produto.objects.filter(exibir_na_home=True)
    return render(request, 'loja/home.html', {'produtos': produtos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == 'adm123' and user.password == 'adm123':
                return redirect('painel')
            return redirect('home')
        else:
            return render(request, 'loja/login.html', {'error': 'Invalid credentials'})
    return render(request, 'loja/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')
    return render(request, 'loja/register.html')

@login_required
def perfil_view(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            return redirect('perfil')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
    return render(request, 'loja/perfil.html', {'user_form': user_form, 'password_form': password_form})

def painel(request):
    if not request.user.is_authenticated or request.user.username != 'adm123':
        return redirect('home')
    produtos = Produto.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'loja/painel.html', {'produtos': produtos})

def produto_novo(request):
    if request.method == 'POST':
        # Processar o formulário do produto
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            # Criar o objeto de Produto
            produto = produto_form.save(commit=False)
            produto.save()
            # Processar as imagens enviadas
            imagens = request.FILES.getlist('imagens')
            for imagem in imagens:
                ImagemProduto.objects.create(produto=produto, imagem=imagem)
            return redirect('painel')  # Redireciona de volta ao painel após adicionar o produto
    else:
        produto_form = ProdutoForm()

    return render(request, 'loja/produto_novo.html', {'produto_form': produto_form})


def produto_editar(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            # Salvar o produto com a imagem enviada
            produto = form.save(commit=False)
            if 'imagem' in request.FILES:
                produto.imagem = request.FILES['imagem']
            produto.save()
            return redirect('painel')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'loja/produto_editar.html', {'form': form, 'produto': produto})



def produto_excluir(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('painel')
    return render(request, 'loja/produto_excluir.html', {'produto': produto})

@login_required
def ver_vendas(request):
    pedidos = Pedido.objects.all()
    return render(request, 'loja/ver_vendas.html', {'pedidos': pedidos})

def ver_graficos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/ver_graficos.html', {'produtos': produtos})

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja/produto_detalhes.html', {'produto': produto})


@login_required  # Para proteger a view apenas para usuários logados, se necessário
def comprar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.produto = produto
            pedido.save()
            return redirect('nota_fiscal', pedido_id=pedido.id)
    else:
        form = PedidoForm()
    
    return render(request, 'loja/comprar_produto.html', {'form': form, 'produto': produto})

@login_required
def nota_fiscal(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'loja/nota_fiscal.html', {'pedido': pedido})

@login_required
def gerenciar_outros_produtos(request):
    if request.user.username != 'adm123':
        return redirect('home')
    
    produtos = Produto.objects.filter(exibir_na_home=False)
    
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST, request.FILES)
        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.exibir_na_home = False
            produto.save()
            return redirect('gerenciar_outros_produtos')
    else:
        produto_form = ProdutoForm()
    
    return render(request, 'loja/gerenciar_outros_produtos.html', {'produtos': produtos, 'produto_form': produto_form})

