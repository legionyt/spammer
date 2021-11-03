import pyautogui
import time


def main(times):
    time.sleep(10)
    for i in range(times):
        pyautogui.typewrite('Betty bought some butter the butter got bitter so betty bought some more butter to make the bitter butter better butter')
        pyautogui.press('enter')


times = input('How many times do you want to spam: ')
main(int(times))



