import os
import time
import random
import keyboard
import mouse

os.system("cls")

CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

banner = (
    CYAN
    + r"""
===========================================================================================================================================================
 $$$$$$\                                $$$$$$$\                      
$$  __$$\                               $$  __$$\                     
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$ | $$$$$$\   $$$$$$$\ 
$$ |$$$$\ $$  __$$\ $$  __$$\ $$  _____|$$$$$$$\ |$$  __$$\ $$  _____|
$$ |\_$$ |$$$$$$$$ |$$ |  \__|\$$$$$$\  $$  __$$\ $$$$$$$$ |\$$$$$$\  
$$ |  $$ |$$   ____|$$ |       \____$$\ $$ |  $$ |$$   ____| \____$$\ 
\$$$$$$  |\$$$$$$$\ $$ |      $$$$$$$  |$$$$$$$  |\$$$$$$$\ $$$$$$$  |
 \______/  \_______|\__|      \_______/ \_______/  \_______|\_______/ """
    + MAGENTA
    + r"""


 /$$      /$$ /$$                                                   /$$$$$$   /$$           /$$      /$$                                                  
| $$$    /$$$|__/                                                  /$$__  $$ | $$          | $$$    /$$$                                                  
| $$$$  /$$$$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$ | $$  \__//$$$$$$        | $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$
| $$ $$/$$ $$| $$| $$__  $$ /$$__  $$ /$$_____/ /$$__  $$|____  $$| $$$$   |_  $$_/        | $$ $$/$$ $$ |____  $$ /$$_____/ /$$__  $$ /$$__  $$ /$$_____/
| $$  $$$| $$| $$| $$  \ $$| $$$$$$$$| $$      | $$  \__/ /$$$$$$$| $$_/     | $$          | $$  $$$| $$  /$$$$$$$| $$      | $$  \__/| $$  \ $$|  $$$$$$ 
| $$\  $ | $$| $$| $$  | $$| $$_____/| $$      | $$      /$$__  $$| $$       | $$ /$$      | $$\  $ | $$ /$$__  $$| $$      | $$      | $$  | $$ \____  $$
| $$ \/  | $$| $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$     |  $$$$$$$| $$       |  $$$$/      | $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$/ /$$$$$$$/
|__/     |__/|__/|__/  |__/ \_______/ \_______/|__/      \_______/|__/        \___/        |__/     |__/ \_______/ \_______/|__/       \______/ |_______/ 
                                                                                                                                                          
                                                                                                                                                                                                                                                                                                
===========================================================================================================================================================
"""
    + RESET
)

keyboard.press_and_release("f11")
print(banner)

mouse.wheel(1)
mouse.wheel(1)
mouse.wheel(1)
mouse.wheel(1)

ABind = input("What is your Anchor Bind? \n }  ")
GBind = input("What is your Glowstone Bind? \n }  ")
TBind = input("What is your Totem Bind? \n }  ")
OBind = input("What is your Obsidian Bind? \n }  ")
CBind = input("What is your Crystal Bind? \n }  ")
DACBind = input("What bind to activate D-tap Macro? \n }  ")
SACBind = input("What bind to activate Anchor Macro? \n }  ")
ACBind = input("What bind to activate Air Anchor Macro? \n }  ")


while True:
    if keyboard.is_pressed(DACBind):
        

        delay_ms = random.randint(40, 50)   # Random delay (Light AC bypass)
        delay_ms2 = random.randint(40, 50)
        spam_delay = random.randint(60, 80)

        time.sleep(0.015)
        keyboard.press_and_release(OBind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()
        time.sleep(delay_ms2 / 1000.0)
        keyboard.press_and_release(CBind)
        time.sleep(0.020)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()
        time.sleep(spam_delay / 1000.0)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()
        time.sleep(spam_delay / 1000.0)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()
        time.sleep(spam_delay / 1000.0)
        mouse.right_click()
        time.sleep(spam_delay / 1000.0)
        mouse.click()

        while keyboard.is_pressed(DACBind): #ANTI SPAM DO NOT REMOVE!!
            time.sleep(0.001)


    if keyboard.is_pressed(SACBind):

        
        delay_ms = random.randint(40, 50)   # Random delay (Light AC bypass)
        delay_ms2 = random.randint(20, 35)
        delay_glowsstone_bug_fix = random.randint(35, 50) # bug fix do not remove

        keyboard.press_and_release(ABind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()
        time.sleep(delay_ms2 / 1000.0)

        keyboard.press_and_release(GBind)
        time.sleep(delay_ms2 / 1000.0)
        mouse.right_click()
        time.sleep(delay_glowsstone_bug_fix / 1000.0)

        keyboard.press_and_release(TBind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()

        while keyboard.is_pressed(SACBind):
            time.sleep(0.001)


    if keyboard.is_pressed(ACBind):
        

        delay_ms = random.randint(40, 50)   # Random delay (Light AC bypass)
        delay_ms2 = random.randint(20, 35)

        keyboard.press_and_release(ABind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()
        time.sleep(delay_ms / 1000.0)
        keyboard.press_and_release(GBind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()
        time.sleep(delay_ms / 1000.0)
        keyboard.press_and_release(ABind)
        time.sleep(delay_ms / 1000.0)
        mouse.right_click()
        time.sleep(0.010)
        mouse.right_click()
        time.sleep(delay_ms2 / 1000.0)
        keyboard.press_and_release(GBind)
        time.sleep(delay_ms2 / 1000.0)
        mouse.right_click()
        time.sleep(delay_ms / 1000.0)
        keyboard.press_and_release(TBind)
        time.sleep(delay_ms2 / 1000.0)
        mouse.right_click()

        
        while keyboard.is_pressed(ACBind): #ANTI SPAM DO NOT REMOVE!!
            time.sleep(0.001)