from gui.main_window import iniciar_janela
from database.db import inicializar_banco

if __name__ == "__main__":
    inicializar_banco()
    iniciar_janela()
