# 난이도 선택 함수

def get_level():
    while True:
        try:
            lev = input("난이도(상/중/하) 중 하나를 선택하여 입력해주세요! : ")
            assert lev=='상' or lev=='중' or lev=='하'
            if lev == "상":
                level = 2
            elif lev == "중":
                level = 4
            elif lev == "하":
                level = 6
            break
        except:
            print("난이도를 잘못 입력하셨어요!!")

    return level