import pyautogui
import time

# Aguardar o Discord ser aberto e a janela ficar ativa
time.sleep(5)  # Ajuste o tempo conforme necessário

# Digitar a mensagem no Discord
mensagem = "Desculpe, mas o usuário [@username] não se encontra no presente no momento, pois está provavelmente ocupado.\n\nAss: Bot do Redstein"
pyautogui.write(mensagem, interval=0.1)

# Pressionar Enter para enviar
pyautogui.press('enter')
