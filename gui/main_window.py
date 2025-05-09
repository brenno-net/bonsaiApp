import tkinter as tk
from tkinter import ttk

def iniciar_janela():
    root = tk.Tk()
    root.title("Bonsai Notes")
    root.geometry("400x300")
    
# Título
    ttk.Label(root, text="🌿 Bonsai Notes", font=("Arial", 18)).pack(pady=10)

    # Botões principais
    ttk.Button(root, text="🌱 Cadastrar Planta", width=30, command=lambda: print("Cadastrar Planta")).pack(pady=5)
    ttk.Button(root, text="📒 Anotações por Planta", width=30, command=lambda: print("Anotar por Planta")).pack(pady=5)
    ttk.Button(root, text="🌤️ Anotações Gerais do Jardim", width=30, command=lambda: print("Anotar Geral")).pack(pady=5)

    root.mainloop()