import pyautogui
import time

#pressiona um atalho do teclado 
#(win + d minimiza janelas e mostra desktop)
pyautogui.hotkey("win", "d")

#pressiona a tecla win
pyautogui.press('win')

#digita um texto onde o curso está
pyautogui.write('chrome')

#pressiona a tecla enter
pyautogui.press('enter')

#faz uma pausa de 2 segundos
time.sleep(2)

#maximiza a janela do chrome
pyautogui.hotkey('win', 'up')

#digita um endereço na url
pyautogui.write('chrome://dino')
pyautogui.press('enter')

while True:
    pyautogui.press('space')
    time.sleep(1)