import pyautogui
from time import sleep as slp
from os import system


def click_automatico():
    while True:
        system("cls")
        pegar_posicao = input("\033[35mDeseja pegar a posição do seu mouse? \n\nS/N \033[0m")

        if pegar_posicao == "S":
            posicao = pyautogui.position()
            system("cls")
            print("Posição armazenada")
            print(f"Posição: {posicao}")
            input_enter = input("")
            system("cls")
            slp(2)
            system("cls")
            continue
        elif pegar_posicao == "N":
            system("cls")
            input_click = input("Digite a posição\nModelo: x=[posição x], y=[posição_y]\n")
            coords = input_click.split(", ")
            x = int(coords[0].split("=")[1])
            y = int(coords[1].split("=")[1])
            slp(1)
            pyautogui.click(x, y)
            print("Local clicado com sucesso")
            slp(2)
            system("cls")
            break
        else:
            print("\033[91mERRO: Você deve digitar uma das opções: S para Sim e N para Não\033[0m")
            continue
