import time, random
import pyautogui as p
# 왼쪽 상단 530, 190
#한 칸 34

def MoveAndClick():
    p.click(button='left')
    p.move(34, 0, duration=0.05)

def NextLine():
    p.move(-34 * 25, 34, duration=0.05)

def ColorChange():
    p.moveTo(20, 830, duration=0.1)
    p.click(button='left')

p.moveTo(530, 190, duration=0.5)
for i in range(25):
    for i in range(25):
        if random.choice([True, False]):
            MoveAndClick()
        else:
            p.move(34, 0, duration=0.05)
    NextLine()

ColorChange() #흰색으로 변환
p.moveTo(20, 545, duration=0.1) # 사각형 모드
p.click(button='left')
#---------------------------------------------------------------
p.moveTo(530, 190, duration=0.1)
p.drag(34 * 7, 34 * 7, duration=0.1)
p.moveTo(530 + 34 * 17, 190, duration=0.1)
p.drag(34 * 7, 34 * 7, duration=0.1)
p.moveTo(530, 190 + 34 * 17, duration=0.1)
p.drag(34 * 7, 34 * 7, duration=0.1)

p.moveTo(530 + 34, 190 + 34, duration=0.1)
p.drag(34 * 4, 34 * 4, duration=0.1)
p.moveTo(530 + 34 * 19, 190 + 34, duration=0.1)
p.drag(34 * 4, 34 * 4, duration=0.1)
p.moveTo(530 + 34, 190 + 34 * 19, duration=0.1)
p.drag(34 * 4, 34 * 4, duration=0.1)
#---------------------------------------------------------------
ColorChange() # 검은색으로 변경
#---------------------------------------------------------------
p.moveTo(530, 190, duration=0.1)
p.drag(34 * 6, 34 * 6, duration=0.1)
p.moveTo(530 + 34 * 18, 190, duration=0.1)
p.drag(34 * 6, 34 * 6, duration=0.1)
p.moveTo(530, 190 + 34 * 18, duration=0.1)
p.drag(34 * 6, 34 * 6, duration=0.1)

p.moveTo(530 + 34 * 2, 190 + 34 * 2, duration=0.1)
p.drag(34 * 2, 34 * 2, duration=0.1)
p.move(-34, -34, duration=0.1)
p.click(button='left')
p.moveTo(530 + 34 * 20, 190 + 34 * 2, duration=0.1)
p.drag(34 * 2, 34 * 2, duration=0.1)
p.move(-34, -34, duration=0.1)
p.click(button='left')
p.moveTo(530 + 34 * 2, 190 + 34 * 20, duration=0.1)
p.drag(34 * 2, 34 * 2, duration=0.1)
p.move(-34, -34, duration=0.1)
p.click(button='left')
#--------------------------------------------------------------
    

p.moveTo(530 + 34 * 16, 190 + 34 * 16, duration=0.1)
p.drag(34 * 4, 34 * 4, duration=0.1)
p.move(-34 * 2, -34 * 2, duration=0.1)
p.click(button='left')
ColorChange()
p.moveTo(530 + 34 * 17, 190 + 34 * 17, duration=0.1)
p.drag(34 * 2, 34 * 2, duration=0.1)
    
ColorChange()
p.moveTo(530 + 34 * 8, 190 + 34 * 6, duration=0.1)
p.drag(34 * 8, 0, duration=0.1)
p.moveTo(530 + 34 * 6, 190 + 34 * 8, duration=0.1)
p.drag(0, 34 * 8, duration=0.1)

p.moveTo(20, 400, duration=0.1)
p.click(button='left')
ColorChange()
p.moveTo(530 + 34 * 9, 190 + 34 * 6, duration=0.1)
for i in range(4):
    p.click(button='left')
    p.move(34 * 2, 0, duration=0.1)
p.moveTo(530 + 34 * 6, 190 + 34 * 9, duration=0.1)
for i in range(4):
    p.click(button='left')
    p.move(0, 34 * 2, duration=0.1)