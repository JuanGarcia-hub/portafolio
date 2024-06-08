import pyautogui

x, y = 950, 1000 

mensaje = "juani kbro"

pyautogui.PAUSE=0.01

for i in range(10):
    pyautogui.click(x, y)
    pyautogui.typewrite(mensaje,interval=0.01)
    pyautogui.press('Enter')