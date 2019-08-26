import pygame
import sys
from pygame.locals import *

# 初始化pygame模块
pygame.init()

# 一个size元组
size = width, height = 1000, 800
# 向左下方移动
speed = [2, 1]
bg = (255, 255, 255)  # RGB

# 创建指定大小的窗口->surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("第一个pygame!")

# 加载图片
pkq = pygame.image.load("pkq.jpg")
# 获得图像的位置矩形
position = pkq.get_rect()

right_head = pkq
left_head = pygame.transform.flip(pkq, True, False)

while True:
    # 事件检测
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                pkq = left_head
                speed = [-2, 0]
            if event.key == K_RIGHT:
                pkq = right_head
                speed = [2, 0]
            if event.key == K_UP:
                speed = [0, -2]
            if event.key == K_DOWN:
                speed = [0, 2]

    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像
        pkq = pygame.transform.flip(pkq, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像(把pkq图像放画到screen对应的position位置上面去)
    screen.blit(pkq, position)
    # 更新界面(内存双缓冲模式 )
    pygame.display.update()
    # pygame.display.flip()

    # 延迟10ms
    pygame.time.delay(10)
