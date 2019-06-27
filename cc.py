def ccheck():
    while True:
        try:
            ready = int(input("모두 읽으셨나요? (모두 읽으셨다면 숫자 0을 눌러주세요) : "))
            assert ready == 0
            if ready==0:
                break
        except ValueError:
            print("잘 못 입력하셨어요")
        except AssertionError:
            print("잘 못 입력하셨어요")
    return 0