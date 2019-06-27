# 함수 설명 : 회원사전 member를 인수로 받아 record가 가장 작은 순으로 화면에 출력해주는 프로시저

def show_rank(member):
    print("─── 최단 기록을 보유한 사람을 공개합니다!!! (플레이 시간 기준(sec)) ───")
    sorted_member=sorted(member.items(), key=lambda x: x[1][3]) # sorted 리턴이 리스트형이야.

    for member in sorted_member:
        record=member[1][3]
        print(" "+str(sorted_member.index(member)+1)+".", member[0],":",str(int(record))+"초")
    print("─────────────────────────────────────-")

