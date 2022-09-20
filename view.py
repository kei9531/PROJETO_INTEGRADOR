#Importar Bibliotecas
import sqlite3 as lite
from datetime import datetime

#conexao com o banco
con = lite.connect('dados.db')

#funcao para inserir inventario
def inserir_form(i):
    with con:
        cur = con.cursor()
        query =  "INSERT INTO INVENTÁRIO (NOME,LOCAL,DESCRICAO,MARCA,DATA_DA_COMPRA"\
            "VALOR_DA_COMPRA,SERIE,IMAGEM) VALUES (?,?,?,?,?,?,?,?,)"
        cur.execute(query,i)

#funcao para deletar um registro
def deletar_form(i):
    with con:
         cur = con.cursor()
         query = "DELETE FROM INVENTÁRIO ID=?"
         cur.execute(query,i)

#funcao para atualizar um registro/LINHA/TUPLA
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE INVENTARIO SET NOME=?,LOCAL=?,MARCA=?"\
            "DATA_DA_COMPRA=?,VALOR_DA_COMPRA=?,SERIE=?,IMAGEM=? WHERE ID=?",
        cur.execute(query,i)

#funcao para ver todos os itens do inventario
def ver_form():
    lista_itens = []
    with con:
       cur = con.cursor()
       cur.execute("SELECT * FROM INVENTARIO ORDER BY NOME")
       rows = cur.fetchall()
       for row in rows:
        lista_itens.append(row)
    return lista_itens

#funcao para vaer apenas um item no inventario
def ver_item(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute ("SELECT * FROM INVENTARIO WHERE ID=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append
        return lista_itens
            