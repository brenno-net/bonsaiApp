import sqlite3

def inserir_planta(nome, especie, local, observacoes, data_registro):
    conn = sqlite3.connect('data/bonsai.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO plantas (nome, especie, local, observacoes, data_registro)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, especie, local, observacoes, data_registro))

    conn.commit()
    conn.close()
