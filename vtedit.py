import tkinter.messagebox as msgbox
from tkinter import *
import vt480

# 변수 정의
funcs = ["0"]
code = "0"

# GUI 부분
root = Tk()
root.title("vt480 전용 편집기")
root.geometry("640x480")

def showinfo():
    msgbox.showinfo("정보", "vt480 programming language editor\nvt480 version 0.9 (230910)\neditor version 0.9\n심심해서 만든 난해한 프로그래밍 언어\n\nmade by 볼타전지🤔")

def showsyntax():
    msgbox.showinfo("문법 알림", "0 : 함수 구분\n1 : 버퍼 번째 함수 실행\n2 : 버퍼 1 감소\n3 : 버퍼값 입력\n4 : 버퍼 1 증가\n5 : 포인터 값을 버퍼값으로 설정\n6 : 포인터 위치 1 감소\n7 : 버퍼값을 포인터 값으로 설정\n8 : 버퍼값 출력 \n9 : 포인터 위치 1 증가")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="문법", command=showsyntax)
menu_file.add_command(label="정보", command=showinfo)
menu.add_cascade(label="파일(F)", menu=menu_file)

label1 = Label(root, text="코드를 입력해주세요")
label1.pack()

txt = Entry(root, width=30)
txt.pack()
txt.insert(END, "")

label2 = Label(root, text="입력값(엔터로 구분하기)")
label2.pack()

txt2 = Text(root, width=30, height=5)
txt2.pack()
txt2.insert(END, "")

label3 = Label(root, text="출력값")
label3.pack()

label4 = Label(root, text="")
label4.pack()

def btncmd():
    # 내용 출력
    global code
    code = txt.get() # 1 : 첫번째 라인, 0 : 0번째 column
    funcs = code.split("0")
    label4.config(text=vt480.dofunc(txt2.get("1.0", END).split("\n"), funcs[0]))

btn = Button(root, text="Run", command=btncmd)
btn.pack()

root.config(menu=menu)
root.mainloop()