import pyautogui as pa
import time
pa.PAUSE = 1

pa.press('win')
pa.write("chrome")
pa.press('enter')
pa.write("https://github.com/")
pa.press('enter')