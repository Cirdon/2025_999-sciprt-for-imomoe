import pyautogui
import time

x, y = 1776, 857 #got from the mouse

for i in range(200): #change the times

    if i%98==0 and i!=0:
        time.sleep(8)

    if i%5==2:
        x += 15
        y += 10
    if i%5==4:
        x -= 5
        y -= 5
    if i%5==0:
        x -= 10
        y -= 5
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    time.sleep(12) #adjusted duration of one time
    pyautogui.click()
    
