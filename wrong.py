import time

def wrong(d_open, p_open, d_keep, p_keep,openkeep,level):

    start=time.time()
    try:
        ans=int(input("Yes(9)/NO(0)를 숫자로 입력해주세요 : "))
        assert ans==9 or ans==0
    except:
        ans=1
        print("잘못 입력하셨습니다. 카드를 한장 잃었습니다.")
        lose = p_keep[-1]
        p_keep.remove(lose)
        d_keep.append(lose)

    end = time.time()
    openkeep+=d_open+p_open
    # 입력 소요시간 thr 계산
    thr=end-start
    thr=format(thr,".2f")
    thr=float(thr)
    # print("start는? ", start)
    # print("end는? ",end)
    # print("thr은? ", thr)

    if level == 2:
        speed = 1.5
    elif level == 4:
        speed = 3
    elif level == 6:
        speed = 5

    if ans==9:
        if len(p_keep) != 0:
            lose = p_keep[-1]
            p_keep.remove(lose)
            d_keep.append(lose)
        print("잘못 입력하셨습니다. 카드를 한장 잃었습니다.")

    # 틀린 상황인데, 틀렸다고 함 --> 만약 내가 2초 안에 이렇게 입력했다면 pass 늦으면 한장을 잃어요'
    elif ans==0:
        if thr <= speed:
            print("Correct!")
        else:
            if len(p_keep)!=0:
                lose = p_keep[-1]
                p_keep.remove(lose)
                d_keep. append(lose)
            print("늦으셨습니다. 카드를 한장 잃었습니다.")
    d_open=[]
    p_open=[]
    time.sleep(1)
    return d_open, p_open, d_keep, p_keep, openkeep