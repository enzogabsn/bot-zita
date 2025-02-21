import pyautogui
import os
from time import sleep

def app():
    while True:
        os.system("cls")
        print("\033[31mDigite o nome do aplicativo que deseja abrir\033[0m")
        print("Exemplo: VSCode")
        app = str(input(""))
        if app == "" or app == " ":
            os.system("cls")
            print("\033[91mERRO: Você deve digitar o nome do seu aplicativo\033[0m")
            sleep(1)
            continue
        print("Abrindo o aplicativo...")
        pyautogui.press("win")
        sleep(1)
        pyautogui.typewrite(app)
        sleep(1)
        pyautogui.press("enter")
        print("\033[32mAplicativo aberto com sucesso!\033[0m")
        sleep(2)
        os.system("cls")
        break
