import keyboard
import funtions
import time as t
import os

def pressione_q():
    print("\nPressione Q para Continuar")
    keyboard.wait('Q')  # Espera até que a tecla 'Q' seja pressionada para continuar
    while True:
        if keyboard.read_event():
            funtions.print_espera.print_espera()  # Chama a função de espera no arquivo print_espera.py
            print("Programa carregado com sucesso!")
            t.sleep(2)
            os.system("cls")
            break
