import sqlite3

conn = sqlite3.connect("meubanco.db")

def inserir_tarefa(conexao, descricao, concluida):
    c = conexao.cursor()
    c.execute('''INSERT INTO tarefas
           (descricao, concluida) VALUES (?, ?)''', (descricao, concluida))
    conexao.commit()
    conexao.close()

inserir_tarefa(conn, "Estudar SQLite" , False)