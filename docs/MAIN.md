# Bot com Pyautogui

Esse bot serve para automatizar e ajudar as pessoas a automatizar o seu dia a dia. O nosso sistema funciona assim: você cria um arquivo na pasta "commands" do projeto, coloque qualquer nome (como pro exemplo: auto_youtube), importe o arquivo no início do arquivo principal, chamado main.py (import funtions.commands.sua_automacao.nome_da_funcao_da_sua_automacao) e no arquivo main.py e procurar pela variável comandos_funcoes conforme o padrão dos outros comandos. O código abaixo vai explicar melhor como funciona:

Para melhor entender como criar seus comandos e utilizalos veja o código abaixo:

```python
import pyautogui
import time as t
import os
import funtions.pegar_posicao
import funtions.app, funtions.site, funtions.click_auto, funtions.sua_automacao

# Tela de boas-vindas
while True:
    os.system("cls")
    print("\033[31m                              -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m")
    print("                                        Bem-vindo ao Bot Zita")
    print("\033[31m                              -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m")
    print("")
    print("Este programa permite automatizar suas tarefas diárias simplesmente digitando um \ncomando no terminal. Por favor, leia o repositório do GitHub para ver todos os comandos que podem ser usados e deixe\numa estrela para nos apoiar.")
    print("\033[34m\nAss: Kornerxes Studios\033[0m")
    print("\nPressione Enter para continuar")
    input_temp = input()
    os.system("cls")
    # Usuário insere o comando desejado
    while True:
        user_input = input("\033[33mDigite o comando desejado: \033[0m")
        os.system("cls")


        # Abrir um aplicativo
        if user_input == "/aplicativo":
            funtions.app.app()  # Chama a função app no arquivo app.py
        # Abrir um site
        elif user_input == "/site":
            funtions.site.abrir_site()  # Chama a função site no arquivo site.py
        elif user_input == "/click":
            funtions.click_auto.click_automatico()  # Chama a função click_auto no arquivo click_auto.py
        elif user_input == "/pegar_posicao":
            funtions.pegar_posicao.pegar_posicao()
        elif user_input == "/sair":
            funtions.exit.sair()
        else:
            print("\033[91mERRO: Você deve digitar um dos comandos válidos\033[0m") # Sistema para repetir o loop de verificação de comando do programa
            t.sleep(2.7)
            os.system("cls")
            continue
```

Observem que na linha **33** nós adicionamos uma condição para caso o usuário digite na linha de comando o seu comando, no caso, você pode escolher, como por exemplo: /youtube, /netflix, /amazon, etc. E na linha **12** do nosso código temos depois de todos esses arquivos o arquivo da sua automação com **pyautogui**, que no exemplo se chama sua_automacao.py. Nunca se esqueca que na hora de criar o arquivo adicione o .py depois do nome dele, para indicar que aquele arquivo está utilizando a extensão do python.
