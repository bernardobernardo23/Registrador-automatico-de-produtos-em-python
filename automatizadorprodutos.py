import pyautogui as pa
import time
import os

pa.hotkey('win', 'e') #hotkey --> atalhos
time.sleep(2)
pa.write("cadastro_produtos")   #nome da pasta que o arquivo esta 
time.sleep(1)
pa.press('enter')
time.sleep(2)
pa.write("app")
time.sleep(1)
pa.press('enter')
time.sleep(5)

with open('produtos.txt', 'r') as arquivo:  #abre o arquivo para leitura -->'r' - read
    for linha in arquivo:
        dados = linha.strip().split(',')   #split(',') --> dividir quando encontrar uma virgula
        
        if len(dados) != 3:
            print(f"Erro na linha: {linha} - Formato incorreto.")
            continue  # Pula a linha com erro e continua com a próxima

        produto, quantidade, preco = dados  
        
        pa.press('tab')  # -->nome
        pa.write(produto)
        time.sleep(1.5)

        pa.press('tab')  # -->quantidade
        pa.write(quantidade)
        time.sleep(1.5)

        pa.press('tab')  # -->preco
        pa.write(preco)
        time.sleep(1.5)

        pa.press('enter')#-->registra
        time.sleep(1.5)

        
        pa.press('tab')  
        pa.press('tab') #--sobe para o nome denovo
