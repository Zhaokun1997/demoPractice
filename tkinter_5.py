from tkinter import *

# 顶层根窗口实例
root = Tk()


def callback():
    print("hello")


# menubar = Menu(root)
# filemenu = Menu(menubar)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="file", menu=filemenu)  # 添加级联

root.config(menu=menubar)

root.mainloop()  # 运行窗口
