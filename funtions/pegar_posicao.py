import pyautogui
from time import sleep
from os import system

def pegar_posicao():
    while True:
        system("cls")
        pegar_posicao = input("\033[35mDeseja pegar a posição do seu mouse? \n\nS/N \033[0m")
        if pegar_posicao == "S":
            posicao = pyautogui.position()
            system("cls")
            print("3")
            sleep(1)
            system("cls")
            print("2")
            sleep(1)
            system("cls")
            print("1")
            sleep(1)
            system("cls")
            print(f"Posição: \033[32mx={posicao.x}, y={posicao.y}\033[0m")
            sleep(2)
            print("\nDigite Enter para terminar o programa")
            input_temp = input("\n")
            system("cls")
            break
        elif pegar_posicao == "N":
            system("cls")
            break
        else:
            system("cls")
            print("\033[91mERRO: Você deve digitar S para Sim e N para Não\033[0m")
            sleep(2)
            continue
