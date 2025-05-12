# main_window.py
# Interface principal da aplicação

import tkinter as tk
from gui.adicionar_planta import abrir_janela_inserir

# Função que inicia a janela principal
def iniciar_janela_principal():
    root = tk.Tk()
    root.title("BonsaiApp")
    root.geometry("300x150")

    # Título
    tk.Label(root, text="Registro de Bonsais", font=("Arial", 16)).pack(pady=10)

    # Botão para adicionar planta
    tk.Button(root, text="Adicionar Planta", command=abrir_janela_inserir).pack(pady=10)

    root.mainloop()
