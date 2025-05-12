# adicionar_planta.py
# interface para inserir os dados de uma nova planta

import tkinter as tk
from tkinter import messagebox
from database.models import inserir_planta
from datetime import datetime

# Função que cria e exibe a janela para adicionar nova planta
def abrir_janela_inserir():
    janela = tk.Toplevel()  # Cria uma nova janela (secundária)
    janela.title("Adicionar Nova Planta")

    # Campo: Nome
    tk.Label(janela, text="Nome:").grid(row=0, column=0, sticky="e")
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    # Campo: Espécie
    tk.Label(janela, text="Espécie:").grid(row=1, column=0, sticky="e")
    entry_especie = tk.Entry(janela)
    entry_especie.grid(row=1, column=1)

    # Campo: Local
    tk.Label(janela, text="Local:").grid(row=2, column=0, sticky="e")
    entry_local = tk.Entry(janela)
    entry_local.grid(row=2, column=1)

    # Campo: Observações (caixa de texto maior)
    tk.Label(janela, text="Observações:").grid(row=3, column=0, sticky="ne")
    entry_obs = tk.Text(janela, height=4, width=30)
    entry_obs.grid(row=3, column=1)

    # Função que será chamada ao clicar no botão "Salvar"
    def salvar():
        nome = entry_nome.get()
        especie = entry_especie.get()
        local = entry_local.get()
        observacoes = entry_obs.get("1.0", tk.END).strip()
        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Verifica se nome e espécie foram preenchidos
        if nome and especie:
            inserir_planta(nome, especie, local, observacoes, data_registro)
            messagebox.showinfo("Sucesso", "Planta registrada com sucesso!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha o nome e a espécie.")

    # Botão para salvar os dados
    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=1, pady=10)
