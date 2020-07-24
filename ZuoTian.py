# 1点击物品栏
# 2右键使用飞行棋飞到指定地点
# 3点击npc领取任务
# 1024*768且系统消息在右侧
# 下面各种栏左侧上起点是708，697右下终点是1027，725
# 921, 387
# 1225, 589

# 1228, 387
# 1243, 589

# 390, 333
# 390, 386
# 127.33
# 2.10.12
import json
import time

import cv2

from DaHuaInterfaceUtil import tian_path, huishou_path
from DisposeBean import FlightBean, TalkBean
from DisposeUtil import read_ispose
from FlightChessUtil import tian_mending_chess
from MouseTwoUtil import MouseTwoUtil

# 飞行棋数据
from PictureUtil import screenshot, dHash, cmpHash

myClassReBuild = json.loads(read_ispose(tian_path + 'ZuoTianFlightChess.txt'))
flight_chess_datas = []
for letter in myClassReBuild:
    flight_chess_datas.append(
        FlightBean(letter['goods_position'], letter['goods_position_x'], letter['goods_position_y'],
                   letter['flight_chess_info'], letter['times_left']))
myClassReBuild = json.loads(read_ispose(huishou_path + 'KeHuiShouProfile.txt'))
kehuishou_datas = []
for letter in myClassReBuild:
    kehuishou_datas.append(TalkBean(letter['talk_type'], letter['talk_describe'], letter['talk_picture']))
mouse = MouseTwoUtil()

# # 吃药
# for hao in range(1, 6):
#     mouse.move_to(hao * 160 - 29, 880)
#     mouse.click_left()
#     # 1点击物品栏
#     mouse.click_function(2)
#     # 2右键使用飞行棋飞到指定地点
#     mouse.select_goods(1, 6)
#     mouse.click_right()
#     mouse.click_function(2)
#     # 最小化客户端
#     mouse.move_to(1160, 10)
#     mouse.click_left()
# # 打开队长客户端
# mouse.move_to(1 * 160 - 29, 880)
# mouse.click_left()

# 做天
for num in range(0, 32):
    # 李靖领取任务
    # 1点击物品栏
    mouse.click_function(2)
    # 2右键使用飞行棋飞到指定地点
    mouse.select_goods(1, 1)
    mouse.click_right()
    mouse.select_option(1)
    tian_mending_chess(flight_chess_datas, 1, 1)
    # 3点击npc领取任务
    time.sleep(2)
    mouse.move_to(350, 140)
    mouse.click_left()
    mouse.select_option(4)

    # 杀三头魔王
    # 1点击物品栏
    mouse.click_function(2)
    # 2右键使用飞行棋飞到指定地点
    mouse.select_goods(1, 2)
    mouse.click_right()
    mouse.select_option(1)
    tian_mending_chess(flight_chess_datas, 1, 2)
    # 3点击npc领取任务
    time.sleep(2)
    mouse.move_to(360, 280)
    mouse.click_left()
    mouse.select_option(1)
    time.sleep(20)

    # 杀黑山妖王
    # 1点击物品栏
    mouse.click_function(2)
    # 2右键使用飞行棋飞到指定地点
    mouse.select_goods(1, 3)
    mouse.click_right()
    mouse.select_option(1)
    tian_mending_chess(flight_chess_datas, 1, 3)
    # 3点击npc领取任务
    time.sleep(2)
    mouse.move_to(405, 220)
    mouse.click_left()
    mouse.select_option(1)
    time.sleep(18)

    # 杀蓝色妖王
    # 1点击物品栏
    mouse.click_function(2)
    # 2右键使用飞行棋飞到指定地点
    mouse.select_goods(1, 4)
    mouse.click_right()
    mouse.select_option(1)
    tian_mending_chess(flight_chess_datas, 1, 4)
    # 3点击npc领取任务
    time.sleep(2)
    mouse.move_to(665, 250)
    mouse.click_left()
    mouse.select_option(1)
    time.sleep(18)

    # 杀万年妖王
    # 1点击物品栏
    mouse.click_function(2)
    # 2右键使用飞行棋飞到指定地点
    mouse.select_goods(1, 5)
    mouse.click_right()
    mouse.select_option(1)
    tian_mending_chess(flight_chess_datas, 1, 5)
    # 3点击npc领取任务
    time.sleep(2)
    mouse.move_to(610, 350)
    mouse.click_left()
    mouse.select_option(1)
    time.sleep(18)

# 去石破烂卖掉垃圾换钱
# 1点击物品栏
mouse.click_function(2)
# 2右键使用飞行棋飞到指定地点
mouse.select_goods(2, 1)
mouse.click_right()
mouse.select_option(1)
tian_mending_chess(flight_chess_datas, 2, 1)
# 3点击npc领取任务
time.sleep(2)
for hao in range(1, 6):
    if hao > 1:
        mouse.move_to(hao * 160 - 29, 880)
        mouse.click_left()
    mouse.click_function(5)
    mouse.move_to(385, 290)
    mouse.click_left()
    mouse.drag_window(640, 200, 240, 200)
    # 相似度
    con = 100
    # 筛选出来的最终结果
    current_task = ''
    # 从第一个开始截图
    for ceng in range(1, 3):
        # 点击物品栏1
        mouse.move_to(394, ceng * 50.5 + 203)
        mouse.click_left()
        for num in range(1, 5):
            for lie in range(1, 7):
                time.sleep(1)
                screenshot(int(lie * 51 + 26 + 9), int(num * 51 + 176 + 15), 49 - 9, 50 - 15, 'temp.jpg')
                img1 = cv2.imread('temp.jpg')
                hash1 = dHash(img1)
                for temp_task in kehuishou_datas:
                    n = cmpHash(hash1, temp_task.imgHash)
                    if n < con:
                        con = n
                        current_task = temp_task
                if con < 3:
                    # 是可以卖的就卖
                    mouse.move_to(lie * 50.5 + 55, num * 50.5 + 203)
                    mouse.click_left()
                    mouse.move_to(300, 530)
                    mouse.click_left()
                con = 100
    # 关闭给与弹窗
    mouse.move_to(410, 190)
    mouse.click_left()
    # 最小化客户端
    mouse.move_to(1160, 10)
    mouse.click_left()
