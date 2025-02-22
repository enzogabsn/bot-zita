import pyautogui
from time import sleep
from os import system


def click_automatico():
    while True:
        system("cls")
        pegar_posicao = input("\033[35mDeseja pegar a posição do seu mouse? \n\nS/N \033[0m")
        
        if pegar_posicao == "S":
            posicao = pyautogui.position()
            system("cls")
            print("\033[32mPosição armazenada\033[0m")
            sleep(2)
            system("cls")
            print(f"Posição: \033[32mx={posicao.x}, y={posicao.y}\033[0m")
            sleep(1.5)
            print("\nPressione Enter para continuar")
            input_enter = input("")
            system("cls")
            clicar = input("\033[35mVocê quer clicar nessa posição para testar?\n\nS/N \033[0m ")
            if clicar == "S":
                sleep(1)
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
                pyautogui.click(posicao)
                print("\033[32mLocal clicado com sucesso!\033[0m")
                sleep(3)
                print("\nPressione Enter para encerrar o programa")
                input_enter_2 = input()
                system("cls")
                break
            elif clicar == "N":
                system("cls")
                pass
            else:
                system("cls")
                print("\033[91mERRO: Você deve digitar S para Sim e N para Não\033[0m")
                sleep(2)
                continue
        elif pegar_posicao == "N":
            system("cls")
            input_click = input("Digite a posição\nModelo: \033[35mx=[posição x], y=[posição_y]\033[0m\n")
            coords = input_click.split(", ")
            x = int(coords[0].split("=")[1])
            y = int(coords[1].split("=")[1])
            sleep(1)
            pyautogui.click(x, y)
            print("\033[32mLocal clicado com sucesso!\033[0m")
            sleep(2)
            system("cls")
            break
        else:
            print("\033[91mERRO: Você deve digitar uma das opções: S para Sim e N para Não\033[0m")
            continue
