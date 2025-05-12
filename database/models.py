# models.py
# codigo para operações de banco de dados SQLite

import sqlite3
import os

# Definir o caminho para o arquivo de banco de dados ".db"
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'bonsais.db')

# Cria a tabela de plantas se ela ainda não existir
def criar_tabela():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS plantas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT NOT NULL,
                local TEXT,
                observacoes TEXT,
                data_registro TEXT
            );
        ''')
        conn.commit()

# Insere uma nova planta no banco de dados
def inserir_planta(nome, especie, local, observacoes, data_registro):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO plantas (nome, especie, local, observacoes, data_registro)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, especie, local, observacoes, data_registro))
        conn.commit()
