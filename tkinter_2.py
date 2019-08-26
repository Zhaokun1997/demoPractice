from tkinter import *


def callback():
    var.set("吹吧你，我才不信呢！")


# 顶层根窗口
root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("您所下载的影片含有未成年人限制内容，\n请满18周岁之后再点击观看!")
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)  # 使内容左对齐
textLabel.pack(side=LEFT)  # 位置左边布局

photo = PhotoImage(file="1.png")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

button = Button(frame2, text="我已经满18周岁", command=callback)  # command为点击事件
button.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

root.mainloop()
