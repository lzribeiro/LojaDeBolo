from django.urls import path
from . import views
from .views import home, login_view, logout_view, register, perfil_view, painel, produto_novo, produto_editar, produto_excluir, ver_vendas, ver_graficos, produto_detalhes, comprar_produto, nota_fiscal, gerenciar_outros_produtos


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('painel/', views.painel, name='painel'),
    path('produto_novo/', views.produto_novo, name='produto_novo'),
    path('produto_editar/<int:produto_id>/', views.produto_editar, name='produto_editar'),
    path('produto_excluir/<int:produto_id>/', views.produto_excluir, name='produto_excluir'),
    path('vendas/', views.ver_vendas, name='ver_vendas'),
    path('ver_graficos/', views.ver_graficos, name='ver_graficos'),
    path('produto/<int:produto_id>/', views.produto_detalhes, name='produto_detalhes'),
    path('comprar/<int:produto_id>/', views.comprar_produto, name='comprar_produto'),
    path('vendas/', views.ver_vendas, name='ver_vendas'),
    path('nota_fiscal/<int:pedido_id>/', views.nota_fiscal, name='nota_fiscal'),
    path('gerenciar_outros_produtos/', views.gerenciar_outros_produtos, name='gerenciar_outros_produtos'),
]