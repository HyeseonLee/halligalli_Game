from load_member import *
from login import *
from freshdeck import *
from correct import *
from wrong import *
from store_member import *
from show_rank import *
from check_answer import *
from print_board import *
from cc import *
from get_level import *
from time import localtime, strftime
def main() :

    d_open=[]
    p_open=[]
    tried=0

    print("Welcome to 3H GameLand~!~!~!:)")
    print("")

    # 1. 로그인 : members.txt 파일에서 멤버 데이터 읽고 --> 로그인절차 통해서 사용자이름, 게임시도횟수, 총play시간, 최단기록, 오른손왼손, 전체멤버사전정보 수집
    username,tries,totalplay,record,member=login(load_member())

    # 2. 메뉴얼 : 게임 설명 - ###############################
    print("")
    print("┌────────────────────── 게 임  설 명 ─────────────────────┐")
    print(" ")
    print(" 1. O,X 할리갈리는 기존의 할리갈리를 응용한 게임입니다. ")
    print(" 2. 게일을 시작할떄 난이도를 선택합니다.")
    print("    난이도에 따라 딜러의 반을속도가 빨라져요. (제한시간이 짧아져요.) ")
    print(" 3. player는 카드가 드롭 될때 마다 제한시간안에 yes! or no! 를 입력해야 합니다. 제한시간안에 ")
    print("    입력하지 않으면 player의 실수로 판단 됩니다. 빠른 속도가 중요해요!!")
    print(" 4. 화면에 같은 문양이 5개 있다면 yes! 아니라면 no! 입니다.")
    print("     같은모양 10개도 no! 입니다.")
    print("")
    print("└──────────────────────────────────────────────────┘")
    ccheck()
    level=get_level()

    # 4. 난이도 선택함수 - ########################################

    d_keep, p_keep = fresh_deck()  # deck에서 딜러와 플레이어에게 카드를 주어요. 이때, [{'rank': '4', 'suit': 'Club'}, {'rank': '5', 'suit': 'Club'},...] 이런식으로 31개의 deck이 [{},{}]로 나누어진다.

    # 6. 게임 PLAY중
    print("")
    print("└──────────────────────────────────────────────────┘")
    print("    ")
    print("───────────── !!! 게 임 시 작 !!!  ────────────")


    openkeep = []
    startmin = strftime("%M", localtime())
    startsec = strftime("%S", localtime())
    gamestart = int(startmin) * 60 + int(startsec)

    tried += 1

    while len(d_keep)!=0 and len(p_keep)!=0:
        print_board(d_keep[0],p_keep[0], d_keep, p_keep, username)

    # keep에서 하나 빼고, open에 넣어주기
        ddel=d_keep[0]
        d_keep.remove(ddel)
        d_open.append(ddel)
        pdel=p_keep[0]
        p_keep.remove(pdel)
        p_open.append(pdel)

        if check_answer(d_open, p_open): # 종을 쳐야할 상황일때!!!!
            d_open, p_open, d_keep, p_keep, openkeep=correct(d_open, p_open, d_keep, p_keep,openkeep,level)
        else: # 종을 쳐야하지 말아야 하는 상황일 떄!!!
            d_open, p_open, d_keep, p_keep, openkeep=wrong(d_open, p_open, d_keep, p_keep,openkeep,level)

    print(" ")
    print("────────────── G A M E O V E R  ─────────────")
    if len(d_keep)!=0:
        print(" ")
        print("ㅠㅠ Y O U , L O S E ㅠㅠ")
    else:
        print(" ")
        print("^0^  Y O U , W I N  ^0^")


    endmin = strftime("%M", localtime())
    endsec = strftime("%S", localtime())
    gameend = int(endmin) * 60 + int(endsec)

    gamethr = gameend - gamestart
    gamethr = format(gamethr, ".1f")
    gamethr =float(gamethr)
    # 15. 게임이 진행되는 동안 tried, playtime을 추적하여 --> 게임이 끝난 뒤 결과를 멤버 사전에 적용하여 수정하고 --> members.txt파일에 저장한다.
    passwd,tries,totalplay,record= member[username]
    totalplay += gamethr
    # 이번 턴에 playtime(플레이 타임)이 record보다 작은경우, record를 playtime으로 교체.
    if gamethr<=record:
        if len(d_keep)==0:
            member[username] = (passwd, int(tries + tried), float(totalplay), float(gamethr))
            print("축하해요!! "+str(int(gamethr))+"초의 신기록을 세우셨군요!!!!!!!!")
    else:
        member[username] = (passwd, int(tries + tried), float(totalplay), float(record))  # tried, playtime 추가해야해,
    store_member(member)

    # 16. 지금까지의 칩 최다 보유 멤버 5명을 보여준다.
    print("")
    show_rank(member)
    while True:
        try:
            print("    ")
            qu=input("한판더 ?  > <  ? (y/n) : ")
            assert qu=='y' or qu=='n'
            break
        except:
            print("다시 입력해줘요 > < !!")
    if qu=='y':
        main()
    else:
        print("안녕히가세요", username+"님 ~!! ")



main()


