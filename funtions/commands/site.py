import os
import funtions
import funtions.commands
import funtions.sair

def site():
    print("Digite o nome do site que deseja abrir: ")
    print("Exemplo: https://www.google.com")
    site = str(input(""))
    os.system(f"start {site}")  # Abre o site
    print("\nSite aberto com sucesso!")
    funtions.sair.sair()
