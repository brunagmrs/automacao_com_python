import pyautogui as pa

#Requer Instalação do Pillow: pip install pillow pyscreeze

#Tirar e Salvar Captura de Tela
pa.screenshot("nome.png")

#Posição na tela de uma imagem
#print(pa.locateOnScreen('nome.png'))

#Verifica a cor e se o pixel coresponde a cor
print(pa.pixel(x=1284, y=49))
print(pa.pixelMatchesColor(1284,49, (193, 195, 189)))
