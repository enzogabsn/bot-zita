import pyautogui
import time as t
import os
import funtions.commands.app, funtions.commands.site, funtions.press_q, funtions.exit, funtions.commands.click_auto

# Tela de boas-vindas

os.system("cls")
print("-="*20)
print("Bem-vindo ao Bot Zita")
print("-="*20)
print("Este programa permite automatizar suas tarefas diárias simplesmente digitando um \ncomando no terminal. Por favor, leia o repositório do GitHub para ver todos os comandos que podem ser usados e deixe\numa estrela para nos apoiar. \n\nAss: Kornerxes Studios")
t.sleep(7)
funtions.press_q.press_q()  # Chama a função press_q

# Usuário insere o comando desejado

user_input = str(input("Digite o comando desejado: "))
os.system("cls")

# Abrir um aplicativo
if user_input == "/aplicativo":
    funtions.commands.app.app()  # Chama a função app no arquivo app.py

# Abrir um site
elif user_input == "/pesquisar":
    funtions.commands.site.site()  # Chama a função site no arquivo site.py

# Sair do programa
elif user_input == "/sair":
    funtions.exit.exit()  # Chama a função exit no arquivo exit.py

elif user_input == "/click":
    funtions.commands.click_auto.click_auto()  # Chama a função click_auto no arquivo click_auto.py
else:
    print("Erro: Comando não encontrado.")
    t.sleep(2)
    os.system("cls")
    funtions.exit.exit()  # Chama a função exit no arquivo exit.py
