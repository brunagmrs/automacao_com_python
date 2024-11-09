import pyautogui as pa

#mostrar a posição do mouse
print(pa.position())

#movimentar o mouse para uma posição em cordenadas
pa.moveTo(800, 300)

#movimentar em relação a posição atual
pa.moveRel(10, 10)

#clicar na posição definida
pa.click(800, 300, clicks=1, interval=1, button='left')

#clicar duas vezes em uma posição
pa.rightClick(800, 300) #botão direito
pa.doubleClick(800, 300) #botão esquerdo

#rolagem
pa.scroll(100) #para cima
pa.scroll(-200) #para baixo