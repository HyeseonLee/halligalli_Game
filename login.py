def login(member):
    # INTRO1 - 이름 입력받기
    name = input("당신의 이름은 무엇인가요? (최대 4글자)(영어로 입력해주세요) : ")
    while len(name)>4 or len(name)==0:
        name = input("당신의 이름은 무엇인가요? (최대 4글자)(영어로 입력해주세요) : ")
    trypasswd = input("비밀번호를 입력해주세요 : ")
    while len(trypasswd)==0:
        trypasswd = input("비밀번호를 입력해주세요(1자리 이상 입력해주세요): ")

    if name in member.keys():
        passwd,tries,totalplay,record=member[name]
        if trypasswd==passwd:
            print(name + "님은 지금까지 총 " + str(tries) + "회 저희 게임을 해주셨어요.")
            print("그 중에서 최단 기록은 "+str(record)+"입니다.")
            return name,tries,totalplay,record,member
        else:
            return login(member)

    else:
        member[name] = (trypasswd, 0, 0, 1000000)
        return name,0,0,1000000,member # (name,tries,totalplay,record,member)가 있는 튜플로 return