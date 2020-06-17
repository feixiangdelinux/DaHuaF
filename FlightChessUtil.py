from MouseUtil import MouseUtil


def mending_chess(flight_chess, flight_chess_datas):
    '''补棋
    :param flight_chess: 需要补的棋子
    :param flight_chess_datas: 所有的棋子
    :return:
    '''
    for i in flight_chess_datas[::-1]:
        if i.flight_chess_info == '备用棋':
            flight_chess_datas.remove(i)
            # 打开物品栏
            MouseUtil.open_inventory()
            # 选择背包1还是背包2
            MouseUtil.select_inventory(i.goods_position)
            # 移动到对应的物品栏位置，右键使用飞行棋
            MouseUtil.select_goods(i.goods_position_x, i.goods_position_y)
            # 选择第二个重做路标
            MouseUtil.receive_task(1, 2)
            # 移动到对应的物品栏位置，右键使用飞行棋
            MouseUtil.move_goods(i.goods_position_x, i.goods_position_y)
            # 选择背包1还是背包2
            MouseUtil.select_inventory(flight_chess.goods_position)
            # 移动到对应的物品栏位置，右键使用飞行棋
            MouseUtil.move_goods(flight_chess.goods_position_x, flight_chess.goods_position_y)
            # 关闭物品栏
            MouseUtil.open_inventory()




