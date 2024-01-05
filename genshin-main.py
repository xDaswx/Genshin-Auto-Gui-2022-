from threading import Thread

import pyautogui
import pydirectinput

import time
import random, tecla
import pythoncom,win32api,win32con,time,win32gui,ctypes,sys
import keyboard as kbd
import pytesseract


images = {
    "mochila": "images/mochila.png",
    "mochila2": "images/mochila2.png",
    "conquista": "images/conquista.png",
    "bule": "images/bulederelacha.png",
    "colocar" : "images/colocar.png",
    "entrar" : "images/entrar.png",
    "confianca" : "images/confianca.png",
    "tesouro" : "images/tesouro.png",
    "reputacao" : "images/reputacao.png",
}



# https://stackoverflow.com/questions/7787120/check-if-a-process-is-running-or-not-on-windows-with-python

def click(loc, delay=0.2, button="left"):
    tecla.PressKey(184)
    pyautogui.moveTo(x=loc[0], y=loc[1], duration=delay, tween=pyautogui.easeInSine)
    pydirectinput.mouseDown()
    time.sleep(0.05)
    pydirectinput.mouseUp()
    time.sleep(0.1)
    tecla.ReleaseKey(184)



def checar(image, delay=0.2, timeout=5, button="left"):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True)
        if loc is not None:
            break
    if loc is None:
        print(f"{image} não encontrado")
        return False
    click(loc, delay, button)
    print(f"{image} encontrado")
    return True


def test():
    hwnd = win32gui.FindWindow(None, "Genshin Impact")
    win32gui.SetForegroundWindow(hwnd)
    x1,y1,x2,y2=win32gui.GetWindowRect(hwnd)
    print(x1,y1,x2,y2)
    time.sleep(1)
    tecla.PressKey(0x11)
    time.sleep(1)
    tecla.ReleaseKey(0x11)
    time.sleep(1)
 
    Thread(target = louc).start()

    checar(image=images.get("mochila2"), delay=0.2, timeout=5, button="left")
    time.sleep(1)
   
    checar(image=images.get("bule"), delay=0.2, timeout=5, button="left")
    time.sleep(1)
    checar(image=images.get("colocar"), delay=0.2, timeout=5, button="left")
    time.sleep(1)
    checar(image=images.get("entrar"), delay=0.2, timeout=5, button="left")
    time.sleep(3)
    checar_se_menu()
    time.sleep(1)
    tecla.PressKey(32)
    time.sleep(0.5)
    tecla.ReleaseKey(32)
    time.sleep(0.5)
    tecla.PressKey(33)
    time.sleep(0.5)
    tecla.ReleaseKey(33)
    time.sleep(3)
    pydirectinput.mouseDown()
    time.sleep(0.05)
    pydirectinput.mouseUp()
    checar(image=images.get("confianca"), delay=0.2, timeout=5, button="left")
    time.sleep(1)
    checar(image=images.get("reputacao"), delay=0.2, timeout=5, button="left")
    time.sleep(1)
    checar(image=images.get("tesouro"), delay=0.2, timeout=5, button="left")
    time.sleep(0.5)
    

def checar_se_menu():
    i = 1
    hwnd = win32gui.FindWindow(None, "Genshin Impact")
    win32gui.SetForegroundWindow(hwnd)
    x1,y1,x2,y2=win32gui.GetWindowRect(hwnd)
    time.sleep(1.5)
    while i <= 100:
        print(i)
        if (pyautogui.locateCenterOnScreen(image=images.get("mochila2"), confidence=0.8, grayscale=True)):
            print("Está na tela")
            break
        else:
            print("Não encontrado na tela")
            time.sleep(2)
            i += 1


#test()

hwnd = win32gui.FindWindow(None, "Genshin Impact")
win32gui.SetForegroundWindow(hwnd)
def giragira():
    tecla.PressKey(32)
    tecla.ReleaseKey(32)
    time.sleep(0.05)
    tecla.PressKey(17)
    tecla.ReleaseKey(17)
    time.sleep(0.05)
    tecla.PressKey(30)
    tecla.ReleaseKey(30)
    time.sleep(0.05)
    tecla.PressKey(31)
    tecla.ReleaseKey(31)
    time.sleep(0.05)
def louc():
    i = 1
    while i <= 15: 
        print(i)
        giragira()
        i += 1

test()