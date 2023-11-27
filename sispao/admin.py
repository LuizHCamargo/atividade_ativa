from django.contrib import admin
from .models import Cliente, Pedido, Produto
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data_pedido', 'nome_cliente', 'data_entrega', 'valor_total')

    def nome_cliente(self, obj):
        return obj.id_cliente.nome

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco', 'qt_estoque')