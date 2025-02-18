import pyautogui
from time import sleep as slp
from os import system

while True:
    system("cls")
    pegar_posicao = input("Deseja pegar a sua posição do mouse antes de clicar?\nS/N ")

    if pegar_posicao == "S":
        posicao = pyautogui.position()
        print("Posição armazenada")
        print(f"Posição: {posicao}")
        input_ = input("")
        clicar_cond = input("Deseja clicar nessa posição? S/N ")
        if clicar_cond == "S":
            print("Clicando...")
            slp(2)
            pyautogui.click(posicao)
            system("cls")
            break
        elif clicar_cond == "N":
            system("cls")
        else:
            system("cls")
            print("Você deve digitar 1 das opções: S para Sim e N para Não")
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
        break

system("cls")
print("Obrigado por usar nosso programa! Caso tenha alguma dúvida sobre algum comando, leia a wiki do nosso repositório do \nGitHub.\nAss: Kornerxes Studios")
slp(5)
system("cls")
exit()
