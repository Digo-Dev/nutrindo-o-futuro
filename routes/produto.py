from flask import Blueprint, render_template, request
from database.Produtos import PRODUTOS


produto_route = Blueprint('produto', __name__)

"""
Rota produtos

    - /produto/ (GET)               -> Lista os produtos.
    - /produto/ (POST)              -> Insere o produto no servidor.
    - /produto/new (GET)            -> renderiza o formulario para criar um novo produto.
    - /produto/<id> (GET)           -> Obter os dados de um produto.
    - /produto/<id> (GET)           -> Renderiza um formulario para editar um produto.
    - /produto/<id> (PUT)           -> atualizar os dados de um produto.
    - /produto/<id>/delete (DELETE) -> Apaga o registro de um produto do servidor.
"""

@produto_route.route('/')  
def listar_produto():
    """Lista os produtos"""
    return render_template('lista_produtos.html', produtos=PRODUTOS)

@produto_route.route('/', methods=['POST'])
def inserir_produto():
    """Insere o produto no servidor."""
    print(request.json)
    return {"ok":"OK"}

@produto_route.route('/new')
def form_produto():
    """Renderiza o formulario para criar um novo produto."""
    return render_template('form_produto.html')

@produto_route.route('/<int:id_produto>')
def detalhe_produto(id_produto):
    """Obter os detalhes de um produto."""
    return render_template('detalhe_produto.html')

@produto_route.route('/<int:id_produto>/edit')
def editar_produto(id_produto):
    """Renderiza um formulario para editar um produto."""
    return render_template('form_edit_produto.html')

@produto_route.route('/<int:id_produto>/update',methods=['PUT'])
def atualizar_produto(id_produto):
    """atualizar os dados de um produto."""
    pass

@produto_route.route('/<int:id_produto>/delete',methods=['DELETE'])
def deletar_produto(id_produto):
    """Apaga o registro de um produto do servidor."""
    pass