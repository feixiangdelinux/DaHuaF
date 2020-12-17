import time

from paohuan.MouseTwoUtil import MouseTwoUtil
from paohuan.MouseUtil import MouseUtil


def mending_chess(flight_chess, flight_chess_datas):
    mouse = MouseUtil()
    '''补棋
    :param flight_chess: 需要补的棋子
    :param flight_chess_datas: 所有的棋子
    :return:
    '''
    for i in flight_chess_datas[::-1]:
        if i.flight_chess_info == '备用棋':
            flight_chess_datas.remove(i)
            # 打开物品栏
            mouse.open_inventory()
            # 选择背包1还是背包2
            mouse.select_inventory(i.goods_position)
            # 移动到对应的物品栏位置，右键使用飞行棋
            mouse.select_goods(i.goods_position_x, i.goods_position_y)
            # 选择第二个重做路标
            mouse.select_option(1, 2)
            time.sleep(4)
            # 移动到对应的物品栏位置，左键点击飞行棋
            mouse.move_goods(i.goods_position_x, i.goods_position_y)
            # 选择背包1还是背包2
            mouse.select_inventory(flight_chess.goods_position)
            # 移动到对应的物品栏位置，右键使用飞行棋
            mouse.move_goods(flight_chess.goods_position_x, flight_chess.goods_position_y)
            # 关闭物品栏
            mouse.open_inventory()
            break


def tian_mending_chess(flight_chess_datas, gx, gy):
    """
    需要补棋就补棋，不需要就把飞行棋次数减一
    :param flight_chess_datas: 所有的棋子信息
    :param position: 需要补棋的位置
    :return:
    """
    mouse = MouseTwoUtil()
    if gx == 1:
        flight_chess = flight_chess_datas[gy - 1]
    else:
        flight_chess = flight_chess_datas[- 1]
    # 飞行器次数-1
    flight_chess.times_left = flight_chess.times_left - 1
    # 如果飞行器次数为零
    if flight_chess.times_left == 0:
        # 打开物品栏，打开随身商店
        mouse.select_prop_bottom(3)
        # 购买飞行棋,关闭随身商店
        mouse.buy_prop(1, 2)
        # 鼠标移动到对应的飞行棋上,重新做路标
        mouse.click_function(2)
        mouse.select_goods(gx, gy)
        mouse.click_right()
        mouse.select_option(2)
        # 1关闭物品栏
        mouse.click_function(2)
        # 把新数据保存
        flight_chess.times_left = 99
