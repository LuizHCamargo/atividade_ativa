from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=11, null=False)
    celular = models.CharField(max_length=11, null=False)
    end_cep = models.CharField(max_length=8)
    end_logradouro = models.CharField(max_length=255)
    end_numero = models.CharField(max_length=10)
    end_complemento = models.CharField(max_length=100)
    end_bairro = models.CharField(max_length=100)
    end_cidade = models.CharField(max_length=100)
    end_uf = models.CharField(max_length=2)
    
class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    qt_estoque = models.IntegerField()
    
class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True, null=False)
    data_entrega = models.DateTimeField(null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, null=False)

class PedidoProdutos(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, null=False)


