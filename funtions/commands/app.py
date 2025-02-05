import shutil
import os

def app():
    print("Digite o nome do aplicativo que deseja abrir")
    print("Exemplo: notepad")
    app = str(input(""))
    if shutil.which(app) is None:  # Verifica se o aplicativo existe
        print(f"Erro: O aplicativo '{app}' não foi encontrado.")
        exit()
    os.system(f"start {app}")  # Abre o aplicativo
    print("Aplicativo aberto com sucesso!")
