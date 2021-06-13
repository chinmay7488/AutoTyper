import pyautogui
import time
import random
import website as wb

#time.sleep(3)
print(pyautogui.size())
time.sleep(2)
#int rev = 0;
# int temp = val;
#wb.button_click('Full')
#pyautogui.click(590,220,duration=0.5)
#pyautogui.hotkey('ctrlleft','a')
#time.sleep(2)
#pyautogui.keyDown('del')
# breakp =pyautogui.keyUp('del')
with open('type.txt') as f:
    lines = f.readlines()
#line_no=0
#random_number = 3 
for l in lines:
   # l= l.lstrip()
    #l=l[2:]
    l= l.lstrip()
    pyautogui.write(l,interval=0.1)
    #line_no=line_no+1
    #if(line_no==random_number):
    #    time.sleep(3)
    #    line_no=0
    #    random_number=random.randint(1, 5)
            
        
#time.sleep(4)
#wb.button_click("Restore")
#time.sleep(1) 
#wb.button_click("Save")

