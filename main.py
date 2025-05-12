# main.py
# Ponto de entrada da aplicação

from gui.main_window import iniciar_janela_principal
from database.models import criar_tabela

# Executado quando o programa é iniciado
if __name__ == "__main__":
    criar_tabela()              # Garante que a tabela de banco de dados exista
    iniciar_janela_principal()  # Inicia a interface gráfica
