from tkinter import *


def showinfor():
    print("作品：《%s》" % e1.get())
    print("作者：《%s》" % e2.get())


root = Tk()

Label(root, text="作品：").grid(row=0, column=0)
Label(root, text="作者：").grid(row=1, column=0)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

Button(root, text="获取信息", width=10, command=showinfor) \
    .grid(row=2, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit) \
    .grid(row=2, column=1, sticky=E, padx=10, pady=5)

mainloop()
