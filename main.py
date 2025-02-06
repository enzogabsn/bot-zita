import pyautogui
import time as t
import os
import keyboard
import shutil
import funtions.commands.app, funtions.commands.site, funtions.pressione_q, funtions.sair




# Tela de boas-vindas

os.system("cls")
print("-="*20)
print("Bem-vindo ao Bot Zita")
print("-="*20)
print("Esse programa serve para você automatizar o seu dia a dia somente digitando um comando no terminal, \npara isso, leia no repositório do GitHub para ver todos os comandos que pode ser utilizados.")
    
funtions.pressione_q.press_q()  # Chama a função pressione_q
    
# Usuário digita o comando desejado

input_usuario = str(input("Digite o comando desejado: "))
os.system("cls")

# Abre um aplicativo
if input_usuario == "/aplicativo":
    funtions.commands.app.app()  # Chama a função app no arquivo app.py

# Abre um site
elif input_usuario == "/site":
    funtions.commands.site.site() # Chama a função site no arquivo site.py
    
    # Sai do programa
elif input_usuario == "/exit":
    funtions.sair.sair()  # Chama a função sair no arquivo sair.py

else:
    print("Erro: Comando não encontrado.")
    t.sleep(2)
    os.system("cls")
    funtions.sair.sair()  # Chama a função sair no arquivo sair.py
