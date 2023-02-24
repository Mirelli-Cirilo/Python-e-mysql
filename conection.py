import mysql.connector

conexao = mysql.connector.connect(host='localhost', user='root', password='987654321')

cur = conexao.cursor()
cur.execute("CREATE DATABASE meubanco")
conexao.close()
