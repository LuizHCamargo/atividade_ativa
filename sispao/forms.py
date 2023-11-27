from django.forms import ModelForm, ModelChoiceField
from .models import Cliente, PedidoProdutos, Produto

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class AcessoForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf'] 

class EscolhaProduto(ModelChoiceField):
    def label(self, obj):
        return obj.descricao
    
class PedidoForm(ModelForm):
    class Meta:
        model = PedidoProdutos
        fields = ['quantidade']
