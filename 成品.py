import threading
import time
import random

gameover=0    #難度設定
cdn = 0
gm=str(input("gamemode: Easy / Normal / Difficult / Crazy :  "))
if gm == "Easy":
    cdn = 40
elif gm == "Normal":
    cdn = 20
elif gm == "Difficult":
    cdn = 10
elif gm == "Crazy":
    cdn = 6
else:
    print("gamemode error")
    
def countdown(num_of_secs):   #倒數計時器
    global gameover
    while num_of_secs:
        if gameover==1:
            exit()
        time.sleep(1)
        num_of_secs -= 1
    gameover = 1
    print("")
    for i in range(0,30):
        print("  Gameover QAQ ")
        print("")
        time.sleep(0.08)
    print("")
    print("  Answer is",ans)

start=1  #範圍
end=100
ans = random.randint(start, end)   #答案

t = threading.Thread(target = countdown, args = (cdn,))  #開始倒數
t.start()

while gameover!=1:   #開始
    print(start,"~",end,":",end="  ")
    num=int(input())
    if gameover==1:
        time.sleep(2.400000001)
        exit()
    elif num>ans:
        end = num-1
    elif num<ans:
        start = num+1
    elif num==ans:
        print("BINGO")
        gameover=1
        exit()
