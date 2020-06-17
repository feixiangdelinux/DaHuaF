import cv2

from DaHuaInterfaceUtil import file_path
from PictureUtil import dHash


def get_pic_hash(task_picture):
    img1 = cv2.imread(file_path + task_picture)
    return dHash(img1)


class FlightBean:
    """飞行棋信息
    """

    def __init__(self, goods_position, goods_position_x, goods_position_y, flight_chess_info, times_left):
        # npc对应的飞行棋哪个包中(一共4个包)
        self.goods_position = goods_position
        # 飞行棋在物品栏的水平位置(1-6)
        self.goods_position_x = goods_position_x
        # 飞行棋在物品栏包的垂直位置(1-4)
        self.goods_position_y = goods_position_y
        # 飞行棋在哪个地图,具体坐标是什么
        self.flight_chess_info = flight_chess_info
        # 飞行棋信息飞行棋所剩次数
        self.times_left = times_left


class DisposeBean:
    """200环任务链信息
    """

    def __init__(self, task_type, task_describe, task_picture, npc_name, window_location_x, window_location_y,
                 flight_chess_info):
        # 任务类型
        self.task_type = task_type
        # 任务描述(文字)
        self.task_describe = task_describe
        # 任务描述(图片)
        self.task_picture = task_picture
        # npc的名称
        self.npc_name = npc_name
        # npc对应的窗口水平位置
        self.window_location_x = window_location_x
        # npc对应的窗口垂直位置
        self.window_location_y = window_location_y
        # 与NPC有关的飞行棋在哪个地图,具体坐标是什么
        self.flight_chess_info = flight_chess_info
        # 图片的哈希值,用来对比图片
        self.imgHash = get_pic_hash(task_picture)


class TalkBean:
    """npc对话的数据模型
    """

    def __init__(self, talk_type, talk_describe, talk_picture):
        # 对话类型
        self.talk_type = talk_type
        # 任务描述(文字)
        self.talk_describe = talk_describe
        # 任务描述(图片)
        self.talk_picture = talk_picture
        # 图片的哈希值,用来对比图片
        self.imgHash = get_pic_hash(talk_picture)
