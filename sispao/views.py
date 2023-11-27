from django.shortcuts import render, redirect
from .forms import AcessoForm, ClienteForm, PedidoForm
from .models import Cliente, Pedido, Produto, PedidoProdutos
# Create your views here.

def acesso(request):
    id_cliente = request.session.get('client_id')
    if id_cliente is not None:
        return redirect('todos_pedidos')
    
    if request.method == 'POST':
        form = AcessoForm(request.POST)
        cliente = None

        try:
            cliente = Cliente.objects.get(cpf=request.POST.get('cpf'))
        except Cliente.DoesNotExist:
            form = ClienteForm()
            return redirect('cadastro_cliente')
        
        request.session['id_cliente'] = cliente.id
        return redirect('todos_pedidos')

    else:
        form = AcessoForm()
        return render(request, 'form_acesso.html', {'form': form})
    

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        cliente = form.save(commit=False)
        cliente.save()
        request.session['id_cliente'] = cliente.id
        return redirect('todos_pedidos')

    else:
        form = ClienteForm()
        return render(request, 'form_cadastro.html', {'form': form})

def lista_pedidos(request):
    id_cliente = request.session.get('id_cliente')
    if id_cliente is None:
        return redirect('acesso')
    
    cliente = Cliente.objects.get(pk=id_cliente)
    pedidos = Pedido.objects.filter(id_cliente=cliente.id)

    return render(request, 'lista_pedidos.html', { 'pedidos': pedidos })

def novo_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        cliente = Cliente.objects.get(pk=request.session.get('id_cliente'))

        pedido = Pedido.objects.create(id_cliente=cliente, valor_total=0)

        produtos = Produto.objects.all()
        valor_total = 0

        for produto in produtos:
            quantidade_prod = f'quantidade_{produto.id}'
            quantidade = int(request.POST.get(quantidade_prod, 0))

            if quantidade > 0:
                pedido_produto = PedidoProdutos.objects.create(
                    id_produto=produto,
                    id_pedido=pedido,
                    quantidade=quantidade
                )
                valor_total = valor_total + (produto.preco * quantidade)

                pedido_produto.save()
        
        pedido.valor_total = valor_total
        pedido.save()
        return redirect('todos_pedidos')

    else:
        form = PedidoForm()
        produtos = Produto.objects.all()
        return render(request, 'form_pedido.html', {'produtos': produtos, 'form': form})
    
