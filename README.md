# Bot com Pyautogui

Olá, e bem-vindo ao meu projeto de automação com Pyautogui! Nesse repositório vou mostrar todos os códigos do meu primeiro bot, espero que seja útil para vocês.

**O que é Pyautogui?**

Pyautogui é uma biblioteca do Python onde ela automatiza cliques, escrita, rolagem nas páginas, etc. Essa biblioteca serve para interagir com o seu computador. Vamos ver um exemplo de código, onde é o nosso primeiro arquivo no repositório:

```python
import pyautogui
import time

# Aguardar o Discord ser aberto e a janela ficar ativa
time.sleep(5)  # Ajuste o tempo conforme necessário

# Digitar a mensagem no Discord
mensagem = "Desculpe, mas o usuário [@username] não se encontra no presente no momento, pois está provavelmente ocupado.\n\nAss: Bot do Redstein"
pyautogui.write(mensagem, interval=0.1)

# Pressionar Enter para enviar
pyautogui.press('enter')
```

Esse código em Python com Pyautogui está disponível no arquivo chamado test.py, onde está a base do nosso bot. Esse código acima serve para que quando der um time de 5 segundos
