from tkinter import *
import math as m

# 顶层根窗口实例
root = Tk()
w = Canvas(root, width=1000, height=500, background="white")
w.pack()

center_x = 500
center_y = 250
r = 50
points = [
    # 左上点
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # 右上点
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # 左下点
    center_x - int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
    # 顶点
    center_x,
    center_y - r,
    # 右下点
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5))
]

w.create_oval(center_x - 1.75 * r, center_y - 1.75 * r, center_x + 1.75 * r, center_y + 1.75 * r, fill="red")
w.create_oval(center_x - 1.5 * r, center_y - 1.5 * r, center_x + 1.5 * r, center_y + 1.5 * r, fill="white")
w.create_oval(center_x - 1.25 * r, center_y - 1.25 * r, center_x + 1.25 * r, center_y + 1.25 * r, fill="red")
w.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, fill="blue")
w.create_polygon(points, outline="black", fill="white")

root.mainloop()  # 运行窗口
