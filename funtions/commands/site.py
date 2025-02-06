import os
import funtions
import funtions.commands
import funtions.exit
import pyautogui
from time import sleep

def site():
    print("Digite o nome do site que deseja abrir ou alguma coisa, como pandas ou coalas: ")
    print("Exemplo: https://www.google.com ou 'pandas'.")
    site = str(input(""))
    # Abre o site
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    sleep(3)
    pyautogui.write(site)
    funtions.exit.sair()
