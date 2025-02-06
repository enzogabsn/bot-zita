import keyboard
import funtions
import time as t
import os

def press_q():
    os.system("cls")
    print("\nPressione Q para Continuar")
    keyboard.wait('Q')  # Espera até que a tecla 'Q' seja pressionada para continuar
    while True:
        if keyboard.read_event():
            t.sleep(0.3)
            os.system("cls")
            break
