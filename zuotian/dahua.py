import time

from pynput.mouse import Button, Controller

from zuotian.MouseUtil import MouseUtil

mouse = Controller()
# 领取任务
# 打开物品栏
mouse.position = (523, 615)
time.sleep(1)
mouse.press(Button.left)
mouse.release(Button.left)
# 使用指定位置的飞行棋飞到指定位置
time.sleep(1)
for i in range(10):
    MouseUtil().select_goods(1, 1)
    time.sleep(1)
    MouseUtil().receive_task()
    # 左键点击npc,领取任务
    time.sleep(2)
    mouse.position = (310, 200)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
    MouseUtil().receive_task()
    time.sleep(3)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # 如果需要补棋,就补棋

    # 杀三头魔王
    # 使用指定位置的飞行棋飞到指定位置
    time.sleep(1)
    MouseUtil().select_goods(1, 2)
    time.sleep(1)
    MouseUtil().receive_task()
    # 左键点击npc,领取任务
    time.sleep(2)
    mouse.position = (190, 300)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(26)

    # 杀黑山妖王
    # 使用指定位置的飞行棋飞到指定位置
    time.sleep(1)
    MouseUtil().select_goods(1, 3)
    time.sleep(1)
    MouseUtil().receive_task()
    # 左键点击npc,领取任务
    time.sleep(2)
    mouse.position = (230, 300)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(26)

    # 杀蓝色妖王
    # 使用指定位置的飞行棋飞到指定位置
    time.sleep(1)
    MouseUtil().select_goods(1, 4)
    time.sleep(1)
    MouseUtil().receive_task()
    # 左键点击npc,领取任务
    time.sleep(2)
    mouse.position = (280, 240)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(26)

    # 杀万年熊王
    # 使用指定位置的飞行棋飞到指定位置
    time.sleep(1)
    MouseUtil().select_goods(1, 5)
    time.sleep(1)
    MouseUtil().receive_task()
    # 左键点击npc,领取任务
    time.sleep(3)
    mouse.position = (480, 580)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(26)
print('任务结束')
