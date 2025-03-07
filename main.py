import pyautogui
import time as t
import os
import funtions.app, funtions.site, funtions.click_auto, funtions.pegar_posicao

# Tela de boas-vindas
while True:
    os.system("cls")
    print("\033[31m                              -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m")
    print("                                        Bem-vindo ao Bot Zita")
    print("\033[31m                              -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m")
    print("")
    print("Este programa permite automatizar suas tarefas diárias simplesmente digitando um \ncomando no terminal. Por favor, leia o repositório do GitHub para ver todos os comandos que podem ser usados e deixe\numa estrela para nos apoiar.")
    print("\nAss: \033[34mKornerxes Studios\033[0m")
    print("\nPressione Enter para continuar")
    input_temp = input()
    os.system("cls")
    # Usuário insere o comando desejado

    while True:
        os.system("cls")
        user_input = input("\033[33mDigite o comando desejado: \033[0m")
        if user_input == "/aplicativo":
            funtions.app.app()  # Chama a função app no arquivo app.py

        elif user_input == "/site":
            funtions.site.abrir_site()  # Chama a função site no arquivo site.py

        elif user_input == "/click":
            funtions.click_auto.click_automatico()  # Chama a função click_auto no arquivo click_auto.py

        elif user_input == "/posicao":
            funtions.pegar_posicao.pegar_posicao() # Chama a função pegar_posicao no arquivo pegar_posicao.py

        elif user_input == "/sair":
            funtions.exit.sair() # Chama a função sair no arquivo exit.py
        else:
            os.system("cls")
            print("\033[91mERRO: Você deve digitar um dos comandos válidos\033[0m") # Sistema para repetir o loop de verificação de comando do programa
            t.sleep(2)
            os.system("cls")
            continue
