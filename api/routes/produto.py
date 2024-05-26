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

    sql = f"insert into produtos values (default,'{Produto}','{Unidade}','{Peso}','{Quantidade}','{Lote}','{Validade}')"
    
    conectar()

    try:
        conexao.is_connected()
        cursor = conexao.cursor()
        cursor.execute(sql)
        (cursor.rowcount, "registros na tabela produto")

        cursor.execute('select * from produtos;')
        produtosBD = cursor.fetchall()
        produtosBD = list(produtosBD)
        cursor.close()
        return redirect('/produto')
    except:
        #modal informando que não foi possivel
        return redirect('/produto')
    
#Apaga o registro de um produto do servidor (Delete).
@produto_route.route('/<int:produto_id>/delete')
def deletar_produto(produto_id):
    id = produto_id
    sql = f"delete from produtos where id = '{id}';"
    
    try:
        conexao.is_connected()
        conectar()
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()    
        print(cursor.rowcount, "Registro(s) apagado(s)")
        
        cursor.execute('select * from produtos;')
        produtosBD = cursor.fetchall()
        produtosBD = list(produtosBD)
        cursor.close()
        return redirect('/produto')
    except:
        #modal informando que não foi possivel
        return redirect('/produto')


#Renderiza o formulario para atualizar.
@produto_route.route('/<int:produto_id>/update', methods=['GET','POST']) 
def form_update_produto(produto_id):
    id = produto_id
    sql = f'select * from produtos where id = "{id}";'

    conectar()
    conexao.is_connected()
    cursor = conexao.cursor()
    cursor.execute(sql)
    produto = cursor.fetchone()
    produto = list(produto)
    print(produto)
    return render_template('form_update_produto.html', produto = produto)


#atualizar os dados de um produto.
@produto_route.route('/update', methods=['GET','POST'])
def update_produto():
    id = request.form.get("id")
    Produto = request.form.get("Produto")
    Unidade = request.form.get("Unidade")
    Peso = request.form.get("Peso")
    Quantidade = request.form.get("Qtd")
    Lote = request.form.get("Lote")
    Validade = request.form.get("Validade")
    sql = f"update produtos set Produto='{Produto}', Unidade='{Unidade}', Peso={Peso}, Qtd='{Quantidade}', Lote='{Lote}', Validade='{Validade}' where id = '{id}';"
    
    try:
        conectar()
        conexao.is_connected()
        cursor = conexao.cursor()
        print(sql)
        cursor.execute(sql)
        conexao.commit()    
        print(cursor.rowcount, "Registro(s) editados(s)")
        cursor.execute('select * from produtos;')
        produtosBD = cursor.fetchall()
        produtosBD = list(produtosBD)
        cursor.close()
        return redirect('/produto')
    except:
        #modal informando que não foi possivel
        return redirect('/produto')
  
    



