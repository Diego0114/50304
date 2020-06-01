import pygame#開啟pygame
import sys#賄賂系統
import random#賄賂隨機函式
from pygame.locals import*#*是指全部
pygame.init()#初始化
greenApple=pygame.image.load("apple.jpg")#讀取apple圖片檔
greenApple=pygame.transform.scale(greenApple,(20,20))
#更改apple圖片檔大小
font=pygame.font.SysFont("Comic Sans Ms",30)#宣告字體
clock=pygame.time.Clock()#宣告時鐘
screen=pygame.display.set_mode((640,480))#宣告視窗和大小x,y
pygame.display.set_caption("癱蝕舌")#視窗名稱(癱蝕舌)
gameOver=False#沒有gameover
score=0
apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]#隨機生成果子
head=[310,90]#把尾巴刪掉，把頭加入第一個位置
body=[]
num=10
for i in range(num):
    body.append([head[0],i*20+head[1]])#把尾巴刪掉，把頭加入第一個位置
while apple[0]==body[0][0] and apple[1]==body[0][1]:
    apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]#隨機生成果子
direction="up"
while True:#讓遊戲持續進行
    for event in pygame.event.get():#接收事件
        #print(event)#顯示接收的事件
        if event.type==QUIT:#如果關掉癱蝕舌
            pygame.quit()#結束pygame
            sys.exit()#結束python
        elif event.type==KEYDOWN:
            if event.key==273 and direction!="down":#避免反向
                direction="up"
            elif event.key==274 and direction!="up":#避免反向
                direction="down"
            elif event.key==275 and direction!="left":#避免反向
                direction="right"
            elif event.key==276 and direction!="right":#避免反向
                direction="left"
            elif event.key==114 and gameOver:#按r重新開始(要game over)
                gameOver=False#沒有gameover
                score=0
                apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]#隨機生成果子
                while apple[0]==body[0:len(body)-1][0] and apple[1]==body[0:len(body)-1][1]:
                    apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]#隨機生成果子
                head=[310,230]#把尾巴刪掉，把頭加入第一個位置
                body=[[310,230]]#把尾巴刪掉，把頭加入第一個位置
                direction="up"
        # elif event.type==MOUSEBUTTONDOWN:
        #     whlie apple[0]<=event.pos[0]<=apple[0]+20 and apple[1]<=event.pos[1]<=apple[1]+20 and not gameOver:
        #         score+=100
        #         #apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]#隨機生成果子
    for a in body[1:]:
        if a[0]==head[0] and a[1]==head[1]:
            gameOver=True#有gameover
    if direction=="up":
        head[1]-=20
    elif direction=="down":
        head[1]+=20
    elif direction=="right":
        head[0]+=20
    elif direction=="left":
        head[0]-=20
    body.insert(0,list(head))#它是二維list
    if head[0]==apple[0] and head[1]==apple[1]:
        score+=1
        apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]
        while apple[0]==body[0:len(body)-1][0] and apple[1]==body[0:len(body)-1][1]:
            apple=[20*(random.randint(0,30))+10,20*(random.randint(0,22))+10]#隨機生成果子
    else:
        body.pop()#拿出最後一個
    if head[0]<10 or head[0]>=630 or head[1]<10 or head[1]>=470:
        gameOver=True
    if gameOver:
        screen.fill((0,0,0))#顏色填滿(紅,綠,藍)
        pygame.draw.rect(screen,(15,50,200),Rect(180,80,60,20))#(畫在哪裡,顏色,(x,y,長,寬))___
        for i in range(70):
            pygame.draw.rect(screen,(15,50,200),Rect(160-i,80+i,20,20))#(畫在哪裡,顏色,(x,y,長,寬))///
        for i in range(90):
            pygame.draw.rect(screen,(15,50,200),Rect(91,149+i,20,20))#(畫在哪裡,顏色,(x,y,長,寬))｜｜｜
        for i in range(140):
            pygame.draw.rect(screen,(15,50,200),Rect(91+i,238,20,20))#(畫在哪裡,顏色,(x,y,長,寬))____
        for i in range(61):
            pygame.draw.rect(screen,(15,50,200),Rect(170+i,198,20,20))#(畫在哪裡,顏色,(x,y,長,寬))____
        for i in range(41):
            pygame.draw.rect(screen,(15,50,200),Rect(230,198+i,20,20))#(畫在哪裡,顏色,(x,y,長,寬))｜｜｜
        pygame.draw.rect(screen,(15,50,200),Rect(380,80,60,20))#(畫在哪裡,顏色,(x,y,長,寬))___
        for i in range(70):
            pygame.draw.rect(screen,(15,50,200),Rect(360-i,80+i,20,20))#(畫在哪裡,顏色,(x,y,長,寬))///
        for i in range(90):
            pygame.draw.rect(screen,(15,50,200),Rect(291,149+i,20,20))#(畫在哪裡,顏色,(x,y,長,寬))｜｜｜
        for i in range(140):
            pygame.draw.rect(screen,(15,50,200),Rect(291+i,238,20,20))#(畫在哪裡,顏色,(x,y,長,寬))____
        for i in range(61):
            pygame.draw.rect(screen,(15,50,200),Rect(370+i,198,20,20))#(畫在哪裡,顏色,(x,y,長,寬))____
        for i in range(41):
            pygame.draw.rect(screen,(15,50,200),Rect(430,198+i,20,20))#(畫在哪裡,顏色,(x,y,長,寬))｜｜｜
    else:#讓gameover不會再畫圖
        screen.fill((0,0,0))#顏色填滿(紅,綠,藍)
        for part in body:
            pygame.draw.rect(screen,(0,100,0),Rect(part[0],part[1],20,20))#畫正方形(畫在哪裡,顏色,(x,y,長,寬))
        screen.blit(greenApple,apple)#畫出(apple,位置)
    scores=font.render(str(score),True,(255,255,255))#產生字
    screen.blit(scores,(0,0))#畫出(字,位置)
    pygame.display.flip()#重新畫圖      
    clock.tick(round (score)+1)#每秒刷幾次