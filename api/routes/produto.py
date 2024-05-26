from flask import Blueprint, render_template, request, redirect
from databases.conectionDB import conectar, conexao


# Declaração da blueprint "produto"
produto_route = Blueprint('produto', __name__)

conectar()
# =====Rotas da blueprint "produto"======

# Lista os produtos do banco de dados (Read).
@produto_route.route('/')
def listar_produto():
    conectar()
    cont = 0
      
    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute('select * from produtos;')
        produtosBD = cursor.fetchall()
        produtosBD = list(produtosBD)
        cursor.close()
        return render_template('lista_produtos.html', produtos=produtosBD)
    else:
        return "Server offline"

    return redirect('/')
    
#Renderiza o formulario para criar um novo produto.
@produto_route.route('/new') 
def form_produto():
    return render_template('form_produto.html')

#Insere um novo produto no BD (Create)
@produto_route.route('/', methods=['POST'])
def inserir_produto():
    Produto = request.form.get("Produto")
    Unidade = request.form.get("Unidade")
    Peso = request.form.get("Peso")
    Quantidade = request.form.get("Quantidade")
    Lote = request.form.get("Lote")
    Validade = request.form.get("Validade")

    novo_produto = f"insert into produtos values (default,'{Produto}','{Unidade}','{Peso}','{Quantidade}','{Lote}','{Validade}')"
    
    conectar()

    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute(novo_produto)
        (cursor.rowcount, "registros na tabela produto")
    
    


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