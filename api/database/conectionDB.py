import mysql.connector

conexao = mysql.connector.connect(host='localhost', database='nutrindofuturo', user='root', password='')

def conectar():
    if conexao.is_connected():
        print("Conected")
        return True
    else:
        print("Não foi possivel conectar")
        return False