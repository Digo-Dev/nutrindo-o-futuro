from flask import Blueprint, render_template, request
from database.conectionDB import conectar, conexao

produto_route = Blueprint('produto', __name__)

"""Lista os produtos"""
@produto_route.route('/')  
def listar_produto():
    global logado

    conectar()
    cont = 0
    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute('select * from produtos;')
        produtosBD = cursor.fetchall()
        produtosBD = list(produtosBD)
        return render_template('lista_produtos.html', produtos=produtosBD)
    else:
        return "Server offline"
    
"""Insere o produto no servidor."""
@produto_route.route('/', methods=['POST'])
def inserir_produto():
    
    data = request.form.get()

    novo_produto = {
        "id" : len(PRODUTOS)+1,
        "Produto" : data['Produto'],
        "Unidade" : data['Unidade'],
        "Peso" : data['Peso'],
        "Qtd" : data['Qtd'],
        "Lote" : data['Lote'],
        "Validade" : data['Validade']
    }

    PRODUTOS.append(novo_produto)

    return render_template('item_produto.html', produto=novo_produto)
    

"""Renderiza o formulario para criar um novo produto."""
@produto_route.route('/new') 
def form_produto():
    return render_template('form_produto.html')

"""Obter os detalhes de um produto."""
@produto_route.route('/<int:id_produto>')
def detalhe_produto(id_produto):
    return render_template('detalhe_produto.html')

"""Renderiza um formulario para editar um produto."""
@produto_route.route('/<int:id_produto>/edit')
def editar_produto(id_produto):
    return render_template('form_edit_produto.html')

"""atualizar os dados de um produto."""
@produto_route.route('/<int:id_produto>/update',methods=['PUT'])
def atualizar_produto(id_produto):
    pass

"""Apaga o registro de um produto do servidor."""
@produto_route.route('/<int:produto_id>/delete',methods=['DELETE'])
def deletar_produto(produto_id):
    global PRODUTOS
    PRODUTOS = [p for p in PRODUTOS if p['id'] != produto_id]

    return {'deleted':'ok'}