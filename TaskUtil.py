# 1截图
# 2根据当前截图和图片库中所有的图片进行匹配
# 3选取相似度最小的那张图片作为最终结果
# 4根据最终筛选的图片,生成当前任务

# 5操作鼠标领取任务

# 6打开物品栏
# 7选择背包1还是背包2
# 8移动到对应的物品栏位置，右键使用飞行棋
# 9使用飞行棋飞到指定地图


# 第一种类型,普通类型
import time

import cv2

from FlightChessUtil import mending_chess
from MouseUtil import MouseUtil
from PictureUtil import screenshot, dHash, cmpHash


def task_one(current_task, flight_chess_datas, talk_datas, current_coordinate):
    '''200环任务一(最简单的任务)
    打开物品,选择飞行棋,飞到指定地图,交任务
    :param current_task:
    :param flight_chess_datas:
    :param talk_datas:
    :param current_coordinate:
    :return:
    '''
    mouse = MouseUtil()
    flight_chess = get_flight_chess_for_task(current_task, flight_chess_datas)
    if current_coordinate != current_task.flight_chess_info:
        # 打开物品栏
        mouse.open_inventory()
        # 选择背包1还是背包2
        mouse.select_inventory(flight_chess.goods_position)
        # 移动到对应的物品栏位置，右键使用飞行棋
        mouse.select_goods(flight_chess.goods_position_x, flight_chess.goods_position_y)
        # 使用飞行棋飞到指定地图
        mouse.receive_task()
        if flight_chess.times_left == 1:
            mending_chess(flight_chess, flight_chess_datas)
            flight_chess.times_left = 99
        else:
            flight_chess.times_left = flight_chess.times_left - 1
        time.sleep(3)
    # 点击NPC
    mouse.click_npc(current_task.window_location_x, current_task.window_location_y)
    # 交任务选择选项一
    complete_task(talk_datas)
    return current_task.flight_chess_info


def task_two(current_task, flight_chess_datas, talk_datas, current_coordinate):
    '''200环任务二(买东西的任务)
    打开物品,打开随身商店,购买相应的物品,关闭随身商店,选择飞行棋,飞到指定地图,交任务
    :param current_task:
    :param flight_chess_datas:
    :param talk_datas:
    :param current_coordinate:
    :return:
    '''
    mouse = MouseUtil()
    # 打开物品栏
    mouse.open_inventory()
    # 打开随身商店
    mouse.carry_store()
    # 购买相应的物品
    if current_task.task_describe == '梅花仙，说自己想要个簪子，你买一个送给他吧。':
        mouse.carry_store_buy(1, 2)
    elif current_task.task_describe == '情花仙子的鞋子丢了，正为此事发愁呢，你去买双布鞋送给他。':
        mouse.carry_store_buy(1, 3)
    elif current_task.task_describe == '庞夫人前几天看上了一件布裙，你买个他当做礼物吧。':
        mouse.carry_store_buy(1, 6)
    elif current_task.task_describe == '秦琼在找一件拿手的武器，你去买一把长枪送给他。':
        mouse.carry_store_buy(3, 3)
    elif current_task.task_describe == '老贾想学习武艺，一直头痛找不到铁拳套，你去买个送给他吧。':
        mouse.carry_store_buy(4, 1)
    flight_chess = get_flight_chess_for_task(current_task, flight_chess_datas)
    if current_coordinate != current_task.flight_chess_info:
        # 7选择背包1还是背包2
        mouse.select_inventory(flight_chess.goods_position)
        # 8移动到对应的物品栏位置，右键使用飞行棋
        mouse.select_goods(flight_chess.goods_position_x, flight_chess.goods_position_y)
        # 9使用飞行棋飞到指定地图
        mouse.receive_task()
        if flight_chess.times_left == 1:
            mending_chess(flight_chess, flight_chess_datas)
            flight_chess.times_left = 99
        else:
            flight_chess.times_left = flight_chess.times_left - 1
        time.sleep(3)
    else:
        # 关闭物品栏物品栏
        mouse.open_inventory()
    # 点击NPC
    mouse.click_npc(current_task.window_location_x, current_task.window_location_y)
    # 交任务选择选项一
    complete_task(talk_datas)
    return current_task.flight_chess_info


def task_three(current_task, flight_chess_datas, current_coordinate):
    '''200环任务三(杀怪的任务)
    打开物品,选择飞行棋,飞到指定地图,点击npc,选择第一个选项杀他,等待30秒
    :param current_task:
    :param flight_chess_datas:
    :param current_coordinate:
    :return:
    '''
    mouse = MouseUtil()
    flight_chess = get_flight_chess_for_task(current_task, flight_chess_datas)
    if current_coordinate != current_task.flight_chess_info:
        # 打开物品栏
        mouse.open_inventory()
        # 选择背包1还是背包2
        mouse.select_inventory(flight_chess.goods_position)
        # 移动到对应的物品栏位置，右键使用飞行棋
        mouse.select_goods(flight_chess.goods_position_x, flight_chess.goods_position_y)
        # 使用飞行棋飞到指定地图
        mouse.receive_task()
        if flight_chess.times_left == 1:
            mending_chess(flight_chess, flight_chess_datas)
            flight_chess.times_left = 99
        else:
            flight_chess.times_left = flight_chess.times_left - 1
        time.sleep(2)
    # 点击Npc
    mouse.click_npc(current_task.window_location_x, current_task.window_location_y)
    # 选择选项一杀他
    mouse.receive_task()
    # 等待30,杀死NPC
    time.sleep(17)
    return current_task.flight_chess_info


def get_flight_chess_for_task(current_task, flight_chess_datas):
    """根据任务获取飞行棋信息
    :param current_task:任务数据
    :param flight_chess_datas:所有的飞行棋数据
    :return:找到的飞行棋
    """
    for temp_flight_chess in flight_chess_datas:
        if current_task.flight_chess_info == temp_flight_chess.flight_chess_info:
            return temp_flight_chess


def complete_task(talk_datas):
    '''完成任务
    :param talk_datas: 根据不同的对话点不同的位置
    :return:
    '''
    mouse = MouseUtil()
    mouse.move_to(400, 40)
    time.sleep(2)
    screenshot(140, 240, 450, 30, 'temp.jpg')
    img1 = cv2.imread('temp.jpg')
    hash1 = dHash(img1)
    con = 100
    # 筛选出来的最终结果
    current_talk = ''
    for temp_talk in talk_datas:
        n = cmpHash(hash1, temp_talk.imgHash)
        if n < con:
            con = n
            current_talk = temp_talk
    if con > 2:
        mouse.submit_task(1, 1)
    else:
        mouse.submit_task(current_talk.talk_type, 1)
