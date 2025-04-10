import pyautogui
import time as t
import os
import funtions.app, funtions.site, funtions.click_auto, funtions.pegar_posicao, funtions.utilitarios

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

    # Mapeamento de comandos para funções
    comando_funcoes = {
        "/aplicativo": funtions.app.app,
        "/site": funtions.site.abrir_site,
        "/click": funtions.click_auto.click_automatico,
        "/posicao": funtions.pegar_posicao.pegar_posicao,
        "/limpar": funtions.utilitarios.limpar_tela,
        "/tecla": funtions.utilitarios.tecla_rapida,
        "/pesquisa": funtions.utilitarios.pesquisa_google,
        "/mouse": funtions.utilitarios.mover_mouse,
    }

    while True:
        os.system("cls")
        user_input = input("\033[33m\nDigite o comando desejado: \033[0m")
        
        if user_input in comando_funcoes:
            try:
                comando_funcoes[user_input]()  # Executa a função correspondente ao comando
            except Exception as e:
                print(f"Erro ao executar o comando '{user_input}': {e}")
        elif user_input == "":
            print("ERRO: Nenhum comando foi digitado.")
        else:
            # Pesquisa por comandos que contenham o texto digitado
            sugestoes = [cmd for cmd in comando_funcoes.keys() if user_input in cmd]
            if sugestoes:
                os.system("cls")
                print("\033[36mSugestões de comandos encontrados:\033[0m")
                for sugestao in sugestoes:
                    print(f" - {sugestao}")
                input()
            else:
                print("ERRO: Comando inválido. Nenhuma sugestão encontrada.")
