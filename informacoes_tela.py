import pyautogui as pa

#Resolução da tela
print(pa.size())

#Verifica se está dentro dos limites da tela
print(pa.onScreen(1000,1000))
