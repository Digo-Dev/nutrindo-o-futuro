import mysql.connector
from mysql.connector import Error as erro

conexao = mysql.connector.connect(host='localhost', database='nutrindofuturo', user='root', password='')

# Comandos responsaveis por se conectar ao bando de dados.
def conectar():
    try:
        conexao.is_connected()
        print("Conected")
        return True
    except erro:
        print("SQL erro: {}".format(erro))
        return False