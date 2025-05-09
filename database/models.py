from .db import conectar

def inserir_planta(nome, especie, data_aquisicao, localizacao, observacoes):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO plantas (nome, especie, data_aquisicao, localizacao, observacoes)
        VALUES (?, ?, ?, ?, ?);
    """, (nome, especie, data_aquisicao, localizacao, observacoes))

    conn.commit()
    conn.close()
