# 함수설명 : 텍스트파일 members.txt에서 한줄씩 읽어서 다음과 같이 이름을 키로 하는 사전을 만든다. {name:(passwd,tries,totalplay,record,hand)}

def load_member():
    file=open("member.txt", "r")
    member={}
    for line in file:
        name,passwd,tries,totalplay,record=line.strip('\n').split(',')
        member[name]=(passwd,int(tries),float(totalplay),float(record))
    file.close()
    return member