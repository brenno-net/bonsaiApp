import tkinter as tk
from tkinter import messagebox
from database.models import inserir_planta
from datetime import datetime

def abrir_janela_inserir():
    janela = tk.Toplevel()
    janela.title("Adicionar Planta")

    # Campos
    tk.Label(janela, text="Nome:").grid(row=0, column=0)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela, text="Espécie:").grid(row=1, column=0)
    entry_especie = tk.Entry(janela)
    entry_especie.grid(row=1, column=1)

    tk.Label(janela, text="Local:").grid(row=2, column=0)
    entry_local = tk.Entry(janela)
    entry_local.grid(row=2, column=1)

    tk.Label(janela, text="Observações:").grid(row=3, column=0)
    entry_obs = tk.Text(janela, height=5, width=30)
    entry_obs.grid(row=3, column=1)

    def salvar():
        nome = entry_nome.get()
        especie = entry_especie.get()
        local = entry_local.get()
        observacoes = entry_obs.get("1.0", tk.END).strip()
        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if nome and especie:
            inserir_planta(nome, especie, local, observacoes, data_registro)
            messagebox.showinfo("Sucesso", "Planta adicionada com sucesso!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha pelo menos o nome e a espécie.")

    # Botão salvar
    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=1, pady=10)
