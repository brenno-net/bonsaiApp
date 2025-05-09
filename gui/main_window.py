#vou ver se faço uma versão com 2 idiomas
import tkinter as tk
from tkinter import ttk, messagebox
from database.models import inserir_planta

#verificar depois um tamanho bom pra janela
def abrir_cadastro_de_planta():
    janela = tk.Toplevel()
    janela.title("Cadastrar nova planta")
    janela.geometry("400x400")
    
    campos = {}
    
    labels = {
        "nome": "Nome da Planta*",
        "especie": "Espécie",
        "data_aquisicao": "Data de Aquisição (dd/mm/aaaa)",
        "localizacao": "Localização",
        "observacoes": "Observações"
    }
    
    for idx, (campo, texto) in enumerate(labels.items()):
        ttk.Label(janela, text=texto).pack(anchor= "w", padx=10, pady=(10 if idx == 0 else 5))
        entrada = tk.Entry(janela, width=50) if campo != "observações" else tk.Text(janela, height=4, width=50)
        entrada.pack(padx=10)
        campos[campo] = entrada
        
    def salvar():
        nome = campos["nome"].get()
        especie = campos["especie"].get()
        data = campos["data_aquisicao"].get()
        local = campos["localizacao"].get()
        obs = campos["observacoes"].get("1.0", "end").strip()
        
        if not nome:
            messagebox.showwarning("Atenção", "nome da planta é obrigatorio")
            return
        
        inserir_planta(nome, especie, data, local, obs)
        messagebox.showinfo("sucesso", f"planta '{nome}' cadastrada com sucesso!")
        janela.destroy()
        
        
    ttk.Button(janela, text="Salvar", command=salvar).pack(pady=15)

def iniciar_janela():
    root = tk.Tk()
    root.title("Bonsai Notes")
    root.geometry("400x300")
    
# Título
    ttk.Label(root, text="🌿 Bonsai Notes", font=("Arial", 18)).pack(pady=10)

    # Botões principais
    ttk.Button(root, text="🌱 Cadastrar Planta", width=30, command=abrir_cadastro_de_planta).pack(pady=5)
    ttk.Button(root, text="📒 Anotações por Planta", width=30, command=lambda: print("Anotar por Planta")).pack(pady=5)
    ttk.Button(root, text="🌤️ Anotações Gerais do Jardim", width=30, command=lambda: print("Anotar Geral")).pack(pady=5)

    root.mainloop()