from django.forms import ModelForm, ModelChoiceField, IntegerField, modelformset_factory
from django.core.exceptions import ValidationError
from .models import Cliente, PedidoProdutos, Produto
import datetime

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
