import os
import pyautogui
from time import sleep

def abrir_site():
    while True:
        os.system("cls")
        print("\033[31mDigite a URL do site que deseja abrir ou algo que queira pesquisar\033[0m")
        print("\033[34mExemplo: youtube.com\033[0m")
        pesquisa = str(input(""))
        os.system("cls")
        if pesquisa == "" or pesquisa == " ":
            print("\033[91mERRO: Você deve digitar algo que queira pesquisar ou\033[0m")
            continue
        # Abre o site
        pyautogui.press('win')
        sleep(1)
        pyautogui.write("google chrome")
        sleep(1)
        pyautogui.press('enter')
        sleep(1.2)
        
        # Aqui você pode mudar em que conta o site será aberto com o pyautogui.click(x=, y=)

        pyautogui.click(x=690, y=604)
        sleep(1.2)
        pyautogui.typewrite(pesquisa)
        sleep(0.4)
        pyautogui.press("enter")
        sleep(2)
        os.system("cls")
        print("\033[32mSite aberto com sucesso\033[0m")
        sleep(2)
        print("\nPressione Enter para terminar")
        input_temp = input()
        os.system("cls")
        break
