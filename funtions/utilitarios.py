import pyautogui
import time as t
import os
import keyboard
import webbrowser

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls")
    print("\033[32mTela limpa com sucesso!\033[0m")
    t.sleep(1)

def tecla_rapida():
    """Simula o pressionamento de teclas de atalho"""
    print("\033[33mDigite a combinação de teclas (ex: ctrl+c):\033[0m")
    teclas = input().lower()
    try:
        keyboard.press_and_release(teclas)
        print("\033[32mTeclas pressionadas com sucesso!\033[0m")
    except:
        print("\033[91mErro ao pressionar as teclas. Verifique se a combinação está correta.\033[0m")
    t.sleep(2)

def pesquisa_google():
    """Abre o Google e realiza uma pesquisa"""
    print("\033[33mDigite o termo de pesquisa:\033[0m")
    termo = input()
    url = f"https://www.google.com/search?q={termo}"
    webbrowser.open(url)
    print("\033[32mPesquisa iniciada no Google!\033[0m")
    t.sleep(1)

def mover_mouse():
    """Move o mouse para uma posição específica"""
    try:
        print("\033[33mDigite a posição X:\033[0m")
        x = int(input())
        print("\033[33mDigite a posição Y:\033[0m")
        y = int(input())
        pyautogui.moveTo(x, y, duration=0.5)
        print("\033[32mMouse movido com sucesso!\033[0m")
    except ValueError:
        print("\033[91mErro: Digite apenas números inteiros.\033[0m")
    t.sleep(1) 
