# 0 : 함수 구분
# 1 : 버퍼 번째 함수 실행
# 2 : 버퍼 1 감소
# 3 : 버퍼값 입력
# 4 : 버퍼 1 증가
# 5 : 포인터 값을 버퍼값으로 설정
# 6 : 포인터 위치 1 감소
# 7 : 버퍼값을 포인터 값으로 설정
# 8 : 버퍼값 출력 
# 9 : 포인터 위치 1 증가

# 변수 정의
vt = "0"
funcs = ["0"]
prt = ""

# 인터프리터 코드

def dofunc(inp0, func):
    global vt
    global funcs
    global prt
    buffer = 0
    point = [0]
    pntdst = 0
    prt = ""
    inpno = 0
    inp=inp0[:]
    for i in range(len(func)):
        vt = func[i]
        if vt == "1":
            dofunc(funcs[buffer])
        if vt == "2":
            buffer -= 1
        if vt == "3":
            if inpno == len(inp):
                buffer = -1
            else:
                buffer = inp[inpno]
                inpno += 1
        if vt == "4":
            buffer += 1
        if vt == "5":
            point[pntdst] = buffer
        if vt == "6":
            if pntdst == 0:
                point.insert(0,0)
            else:
                pntdst -= 1
        if vt == "7":
            buffer = point[pntdst]
        if vt == "8":
            prt+=str(buffer)# chr(buffer)
        if vt == "9":
            if pntdst + 1 == len(point):
                point.append(0)
            pntdst += 1
    return prt
