import pyautogui as pa

#Digita um texto
pa.typewrite('texto')

#Pressiona uma tecla
pa.press('enter')

#Pressiona ou Solta uma tecla sem alterar entre estados
pa.keyDown('win') #Segura a tecla
pa.keyUp('win') #Solta a tecla

#Combinação de teclas
pa.hotkey('ctrl', 'v')
