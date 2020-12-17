import json

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


# 如果需要补棋,就补棋
flight_chess = get_flight_chess_for_position(1, 4)
if flight_chess.times_left == 0:
    MouseUtil().replenish_piece(flight_chess.goods_position_x, flight_chess.goods_position_y)
    flight_chess.times_left = 30
else:
    flight_chess.times_left = flight_chess.times_left - 1
for temp_flight_chess in flight_chess_datas:
    print(temp_flight_chess.times_left)
print('任务结束')
