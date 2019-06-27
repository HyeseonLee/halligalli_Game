import random
import time

def correct(d_open, p_open, d_keep, p_keep,openkeep,level): #d_open이랑 p_open을 함수 변수로 받아와야해.
    global ans
    start=time.time()
    try:
        ans=int(input("Yes(9)/NO(0)를 숫자로 입력해주세요 : "))
        assert ans==9 or ans==0
    except:
        ans=1
        print("잘못 입력하셨습니다. open된 모든 카드가 딜러에게 넘어 갑니다.")
        openkeep += d_open + p_open
        random.shuffle(openkeep)
        d_keep+=openkeep
    end=time.time()

    openkeep+=d_open+p_open
    d_open=[]
    p_open=[]
    random.shuffle(openkeep)

    thr=end-start
    thr=format(thr,".2f")
    thr=float(thr)

    if level==2:
        speed=1.5
    elif level==4:
        speed=3
    elif level==6:
        speed=5

    # 정답인 상황인데, 맞다고 함 --> 만약 내가 5초 안에 이렇게 입력했다면 Open된 모든 카드가 나한테 와. 아니면 딜러한테 가
    if ans==9:
        if thr<=speed :
            p_keep+=openkeep
            print("open된 모든 카드들을 얻었습니다!!")
        else:
            d_keep+=openkeep
            print("늦으셨습니다. open된 모든 카드들을 잃었습니다!!")
    # 정답인 상황인데, 틀렸다고 함 --> 그 Open된 모든 카드가 다 딜러한테 가
    elif ans==0:
        d_keep+=openkeep
        print("모든 open된 카드들을 잃었습니다!!")
    openkeep = []
    time.sleep(1)
    return d_open, p_open, d_keep,p_keep,openkeep