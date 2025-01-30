import pyautogui
import time as t
import os
import keyboard
import shutil

def print_espera():
    os.system("cls")
    print("Aguarde um momento, o processo está sendo executado.")
    t.sleep(1)
    os.system("cls")
    print("Aguarde um momento, o processo está sendo executado..")
    t.sleep(1)
    os.system("cls")
    print("Aguarde um momento, o processo está sendo executado...")
    t.sleep(1)
    os.system("cls")
    print("Aguarde um momento, o processo está sendo executado.")
    t.sleep(1)
    os.system("cls")
    print("Aguarde um momento, o processo está sendo executado..")
    t.sleep(1)
    os.system("cls")
    print("Aguarde um momento, o processo está sendo executado...")
    t.sleep(1)
    os.system("cls")
    print("Carregando.")
    t.sleep(1)
    os.system("cls")
    print("Carregando..")
    t.sleep(1)
    os.system("cls")

def main():
    print("-="*20)
    print("Bem-vindo ao Bot Redstain")
    print("-="*20)
    print("Esse programa serve para você automatizar o seu dia a dia somente digitando um comando no terminal, \npara isso, leia no repositório do GitHub para ver todos os comandos que pode ser utilizados.")
    
    print("Pressione Q para Continuar")
    keyboard.wait('Q')  # Espera até que a tecla 'esc' seja pressionada para sair do loop
    while True:
        if keyboard.read_event():
            print_espera()
            print("Carregado")
            os.system("cls")
            break
    print("Qual tipo de sistema você deseja abrir?")
    print("1 - Aplicativo")
    print("2 - Site")
    print("3 - Sair")
    input_usuario = str(input("Digite o número correspondente: "))

    if input_usuario == "1":
        print("Digite o nome do aplicativo que deseja abrir: ")
        print("Exemplo: notepad")
        app = str(input("Digite o nome do aplicativo: "))
        if shutil.which(app) is None:
            print(f"Erro: O aplicativo '{app}' não foi encontrado.")
            exit()
        os.system(f"start {app}")
        print("Aplicativo aberto com sucesso!")
    elif input_usuario == "2":
        print("Digite o nome do site que deseja abrir: ")
        print("Exemplo: https://www.google.com")
        site = str(input("Digite o nome do site: "))
        os.system(f"start {site}")
        print("Site aberto com sucesso!")
    elif input_usuario == "3":
        print("Saindo do programa.")
        t.sleep(2)
        os.system("cls")
        print("Saindo do programa..")
        t.sleep(2)
        print("Obrigado por usar nosso programa!")
        exit()
        os.system("cls")
main()
