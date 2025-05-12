import sqlite3
import os

CAMINHO_BANCO = os.path.join("data", "bonsai.db")

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def inicializar_banco():
    if not os.path.exists("data"):
        os.makedirs("data")

    conn = conectar()
    cursor = conn.cursor()

    # Tabela de Plantas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plantas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT,
            local TEXT,
            observacoes TEXT
        );
    """)

    # Tabela de Anotações Gerais do Jardim
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anotacoes_gerais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            clima TEXT,
            temperatura TEXT,
            umidade TEXT,
            observacoes TEXT
        );
    """)

    # Tabela de Anotações por Planta
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anotacoes_plantas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            planta_id INTEGER,
            data TEXT NOT NULL,
            local TEXT,
            observacoes TEXT,
            FOREIGN KEY(planta_id) REFERENCES plantas(id)
        );
    """)

    conn.commit()
    conn.close()
