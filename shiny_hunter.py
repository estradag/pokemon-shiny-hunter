import os
import time

import pyautogui

# bring mgba window to focus
os.system('xdotool search --name "mGBA - POKEMON EMER" | xargs xdotool windowactivate')
# os.system('xdotool search --name "mGBA - POKEMON EMER - 0.8-27-4b92176" | xargs xdotool windowactivate')

# zubat = 1828, 558 | 148, 181, 99
# makuhita = 1830, 548 | 255, 90, 74
# aron = 1852, 602 | 255, 123, 82
# abra = 1852. 582 | 206, 181, 181
# sableye = 1816, 572 | 247, 198, 165

pokemon_coords = [(1288,558), (1830, 548), (1852, 602), (1852, 582), (1816, 572)]
shiny_colors = [(148, 181, 99), (255, 90, 74), (255, 123, 82), (206, 181, 181), (247, 198, 165)]

# sprite measures 64 x 64
# sprite starts at 299, 81, top left corner

# hp   1562, 564 | (82, 107, 99)
# star 1808, 570 | (255, 222, 140)
while(True):
    with pyautogui.hold('up'):
        print('holding up')
        time.sleep(1)
    im = pyautogui.screenshot(region=(0, 0, 3440, 1440))
    print('waiting 3 second')
    time.sleep(3)
    if im.getpixel((1562,564)) == (82, 107, 99):
        for coords in pokemon_coords:
            if im.getpixel(coords) in shiny_colors:
                print("It's a shiny!")
                exit()
        print('waiting 3 seconds before starting')
        time.sleep(3)
        pyautogui.keyDown('x')
        print('pressing x to start')
        time.sleep(3)
        pyautogui.keyUp('x')
        pyautogui.keyDown('right')
        print('pressing right')
        time.sleep(1)
        pyautogui.keyUp('right')
        pyautogui.keyDown('down')
        print('pressing down')
        time.sleep(1)
        pyautogui.keyUp('down')
        pyautogui.keyDown('x')
        print('pressing x to run')
        time.sleep(1)
        pyautogui.keyUp('x')
        pyautogui.keyDown('x')
        print('pressing x to confirm')
        pyautogui.keyUp('x')
    os.system('rm .screenshot*')
