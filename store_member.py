# 함수설명 : 이름을 키로 하는 사전 member를 미리 정한 형식으로 텍스트 파일 member.txt에 씀(저장함)

def store_member(member):
    file=open("member.txt","w")
    names=member.keys() #.keys()는
    for name in names:
        passwd,tries,totalplay,record=member[name]
        line=name+','+passwd+','+str(tries)+','+str(totalplay)+","+str(record)+'\n'
        file.write(line)
    file.close()
