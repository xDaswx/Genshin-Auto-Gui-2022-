from threading import Thread

import pyautogui,pydirectinput,win32gui,time,tecla


icons = {
        "nexus":"",
        "coop_vs_bot":"wildrift/coop.png",
        "check":"wildrift/menu_detectar.png",
        "garen":"",
        "normal_match":"wildrift/normal_match.png",
        "play":"wildrift/play.png",
        "introducao":"wildrift/introducao.png",
        "encontrar":"wildrift/encontrar_partida.png",
        "torre_pequena":"wildrift/torre_minuscula.png",
        "chao":"wildrift/chao.png",
        "minion_vida":"wildrift/minion_vida.png",
        "aceitar":"wildrift/aceitar.png",
        "confirmar":"wildrift/confirmar.png",
         }   


def check_imagem(image):
    i = 0
    if pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True):
       time.sleep(1)
       print(f"{image} ok ")
       return pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True)
    else:
        while i <= 10:
            if not pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True):
                time.sleep(0.8)
                print(f"{image}: Not found, {i}")
                i += 1

            else:
                print(f'{image} found!')
                return pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True)
                
        return False


def match():
    print( 'a')

def create_a_match():

       pyautogui.moveTo(check_imagem(icons.get("normal_match")), duration=0.2, tween=pyautogui.easeInSine)
       pydirectinput.mouseDown()
       time.sleep(0.05)
       pydirectinput.mouseUp()
       #---detectar o botao coop

       time.sleep(0.5)
       pyautogui.moveTo(check_imagem(icons.get("coop_vs_bot")), duration=0.2, tween=pyautogui.easeInSine)
       pydirectinput.mouseDown()
       time.sleep(0.05)
       pydirectinput.mouseUp()
       time.sleep(0.8)
       #---detectar o botao introducao

       pyautogui.moveTo(check_imagem(icons.get("introducao")), duration=0.2, tween=pyautogui.easeInSine)
       pydirectinput.mouseDown()
       time.sleep(0.05)
       pydirectinput.mouseUp()
       time.sleep(0.8)
       #---detectar o botao partida

       #---encontrar partida
       pyautogui.moveTo(check_imagem(icons.get("encontrar")), duration=0.2, tween=pyautogui.easeInSine)
       pydirectinput.mouseDown()
       time.sleep(0.05)
       pydirectinput.mouseUp()
       time.sleep(0.8)
       accept()

def accept():
    aceitar = pyautogui.locateCenterOnScreen(image=icons.get("confirmar"), confidence=0.8)
    while True:
        time.sleep(1)
        if not aceitar:
            print("Aceitar not found")
        else:
            time.sleep(1)
            pyautogui.moveTo(aceitar, duration=0.2)
            pyautogui.click(aceitar)
            break


def champ():
    garen = pyautogui.locateCenterOnScreen(image=icons.get("aceitar"), confidence=0.8)

def torre():
    torre = pyautogui.locateCenterOnScreen(image=icons.get("torre_pequena"), confidence=0.8)
    if torre:
        print("torre found")
        pyautogui.moveTo(torre, duration=0.2, tween=pyautogui.easeInSine)
        pydirectinput.mouseDown()
        time.sleep(0.05)
        pydirectinput.mouseUp()
        time.sleep(0.8)
        while True:
            if not check_imagem(icons.get("chao")):
                time.sleep(1)
                pass
            else:
                break
        print("tecla w")
        tecla.PressKey(17)
        time.sleep(12)
        tecla.ReleaseKey(17)
    else:
        print("não")


def menu_check():
    play = check_imagem(icons.get("play"))
    if play:
       pyautogui.moveTo(x=play[0], y=play[1], duration=0.2, tween=pyautogui.easeInSine)
       pydirectinput.mouseDown()
       time.sleep(0.05)
       pydirectinput.mouseUp()
       #---checar botão normal game---
       time.sleep(1)
       create_a_match()


def minion():
    minion = pyautogui.locateCenterOnScreen(image=icons.get("minion_vida"), confidence=0.8, grayscale=True)
    if minion:
        print(minion)



hwnd = win32gui.FindWindow(None, "LDPlayer")
win32gui.SetForegroundWindow(hwnd)
x1,y1,x2,y2=win32gui.GetWindowRect(hwnd)

menu_check()