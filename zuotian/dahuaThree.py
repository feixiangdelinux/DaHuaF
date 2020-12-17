import json
import time

from pynput.mouse import Controller

from zuotian.DisposeBean import FlightBean
from zuotian.DisposeUtil import read_ispose
from zuotian.MouseUtil import MouseUtil

file_path = 'E://Dahua/'
mouse = Controller()
# 飞行棋数据
myClassReBuild = json.loads(read_ispose(file_path + 'FlightChessProfile.txt'))
flight_chess_datas = []
for letter in myClassReBuild:
    flight_chess_datas.append(
        FlightBean(letter['goods_position'], letter['goods_position_x'], letter['goods_position_y'],
                   letter['flight_chess_info'], letter['times_left']))


def get_flight_chess_for_position(y, x):
    '''
    根据位置获取飞行棋信息
    :param y: 1-4
    :param x: 1-6
    :return: 找到的飞行棋
    '''
    for temp_flight_chess in flight_chess_datas:
        if temp_flight_chess.goods_position_x == y and temp_flight_chess.goods_position_y == x:
            return temp_flight_chess


def replenish_piece(y, x):
    flight_chess.times_left = flight_chess.times_left - 1
    if flight_chess.times_left == 0:
        MouseUtil().replenish_piece(2, 2, y, x)
        flight_chess.times_left = 10
    print(flight_chess.times_left)


# 打开物品栏
MouseUtil().open_inventory()
# 使用飞行棋飞到目的地
MouseUtil().fly_destination(1, 1)
time.sleep(1)
# 左键点击npc,领取任务
MouseUtil().click_npc(310, 200)
MouseUtil().receive_task()
time.sleep(3)
MouseUtil().click_left()
# 如果需要补棋,就补棋
flight_chess = get_flight_chess_for_position(1, 1)
replenish_piece(flight_chess.goods_position_y, flight_chess.goods_position_x)

# 杀三头魔王
# 使用指定位置的飞行棋飞到指定位置
MouseUtil().fly_destination(1, 2)
# 左键点击npc,领取任务
time.sleep(2)
MouseUtil().click_npc(190, 300)
time.sleep(26)
# 如果需要补棋,就补棋
flight_chess = get_flight_chess_for_position(1, 2)
replenish_piece(flight_chess.goods_position_y, flight_chess.goods_position_x)

# 杀黑山妖王
# 使用指定位置的飞行棋飞到指定位置
MouseUtil().fly_destination(1, 3)
# 左键点击npc,领取任务
time.sleep(2)
MouseUtil().click_npc(230, 300)
time.sleep(26)
# 如果需要补棋,就补棋
flight_chess = get_flight_chess_for_position(1, 3)
replenish_piece(flight_chess.goods_position_y, flight_chess.goods_position_x)

# 杀蓝色妖王
# 使用指定位置的飞行棋飞到指定位置
MouseUtil().fly_destination(1, 4)
# 左键点击npc,领取任务
time.sleep(2)
MouseUtil().click_npc(280, 240)
time.sleep(26)
# 如果需要补棋,就补棋
flight_chess = get_flight_chess_for_position(1, 4)
replenish_piece(flight_chess.goods_position_y, flight_chess.goods_position_x)

# 杀万年熊王
# 使用指定位置的飞行棋飞到指定位置
MouseUtil().fly_destination(1, 5)
# 左键点击npc,领取任务
time.sleep(2)
MouseUtil().click_npc(480, 580)
time.sleep(26)
# 如果需要补棋,就补棋
flight_chess = get_flight_chess_for_position(1, 5)
replenish_piece(flight_chess.goods_position_y, flight_chess.goods_position_x)