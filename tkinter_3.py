from tkinter import *

root = Tk()

group = LabelFrame(root, text="最美的古代美女是？")

GirlsList = [("西施", 1), ("貂蝉", 2), ("王昭君", 3), ("杨玉环", 4)]

v = IntVar()
v.set(1)
for girl, num in GirlsList:
    radioButton = Radiobutton(group, text=girl, variable=v, value=num)
    radioButton.pack(anchor=W)

group.pack()

mainloop()
