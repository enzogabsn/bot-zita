# **🤖 Bot com Pyautogui 🚀**  

🎉 **Bem-vindo ao meu projeto de automação com Pyautogui!**  
Aqui você encontrará todos os códigos do meu primeiro bot! Espero que ele seja útil para você. 💡  

---

## **🤔 O que é Pyautogui?**  
🔥 O **Pyautogui** é uma biblioteca incrível em Python que permite automatizar interações com o seu computador, como:  

🖱️ **Movimentação e clique do mouse**  
⌨️ **Digitação de textos automaticamente**  
📸 **Captura de tela**  
📜 **Rolagem de páginas**  
⚙️ **Ações combinadas para automação total**  

---

## **⚙️ Requisitos para usar o projeto**  

🛠️ Certifique-se de ter o seguinte configurado:  

1️⃣ **🐍 Python 3.6 ou superior instalado:**  
👉 Baixe [neste link](https://www.python.org/downloads/).  

2️⃣ **📦 Instale a biblioteca Pyautogui:**  
Digite no terminal:  
```bash
pip install pyautogui
```  

3️⃣ **🖥️ Requisitos adicionais:**  
✅ Sistema operacional Windows, MacOS ou Linux compatível  
✅ Permissões para acesso ao controle do mouse e teclado (caso solicitado)  
✅ Editor de código recomendado: **VSCode** ou **PyCharm**  

---

## **💻 Exemplo de código do bot**  

```python
import pyautogui
import time

# ⏰ Espera 5 segundos para garantir que a janela esteja ativa
time.sleep(5)  

# ✍️ Digitar a mensagem no Discord
mensagem = "Desculpe, mas o usuário [@username] não se encontra no presente no momento, pois está provavelmente ocupado.\n\nAss: 🤖 Bot do Redstein"
pyautogui.write(mensagem, interval=0.1)

# 📤 Pressionar Enter para enviar
pyautogui.press('enter')
```  

---

## **📋 Explicação do Código**  

1️⃣ ⏳ Aguarda **5 segundos** para garantir que a janela do Discord esteja ativa.  
2️⃣ ✍️ Digita automaticamente a mensagem desejada, caractere por caractere.  
3️⃣ 🚀 Pressiona **Enter** para enviar a mensagem automaticamente.  

---

## **📁 Arquivos no Repositório**  
📄 **test.py:** Contém a base do bot descrita acima.  

---

## **💡 Dicas Importantes**  
🔐 **Segurança:** Automatize com responsabilidade e evite ações que possam prejudicar seu sistema.  
🛠️ **Personalização:** Altere a mensagem e o tempo de espera para se adaptar à sua necessidade.  

---

## **⭐ Apoie o Projeto!**  
Se gostou do projeto, deixe uma **estrela** para apoiar! |⭐| 
