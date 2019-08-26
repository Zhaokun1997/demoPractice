import pygame
import sys

# 初始化pygame模块
pygame.init()

# 一个size元组
size = width, height = 1000, 800
bg = (0, 0, 0)
font = pygame.font.Font(None, 20)
position = 0
line_height = font.get_linesize()

# 创建指定大小的窗口->surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("pygame事件测试!")

screen.fill(bg)

while True:
    # 事件检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()
