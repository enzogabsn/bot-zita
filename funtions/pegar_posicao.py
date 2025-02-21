import pyautogui
from time import sleep
from os import system

def pegar_posicao():
    while True:
        system("cls")
        confirm = input("Você deseja pegar a posição do seu mouse?\n\nS/N ")
        if confirm == "S":
            pass
        elif confirm == "N":
            break
        else:
            print("\033[31mERRO: Você deve escolher uma das opções ditas: S para Sim e N para não\033[0m")
            continue
        posicao = pyautogui.position()
        system("cls")
        sleep(1)
        print("3.")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        system("cls")
        print(f"Posição: {posicao}")
        sleep(2)
        print("Digite Enter para terminar o programa")
        input_temp = input()
        system("cls")
        break
