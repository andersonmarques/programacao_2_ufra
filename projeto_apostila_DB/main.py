import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sqlite3

conn = sqlite3.connect("meubanco.db")#cria o banco de dados

c = conn.cursor()#cria o cursor, que é o objeto que permite executar comandos SQL
#cria a tabela tarefas
c.execute('''CREATE TABLE tarefas
        (id INTEGER PRIMARY KEY, descricao TEXT, concluida BOOLEAN)''')
conn.commit()#salva as alterações
conn.close()#fecha a conexão com o banco de dados
