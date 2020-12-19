class FlightBean:
    """飞行棋信息
    """

    def __init__(self, goods_position,goods_position_x, goods_position_y,  flight_chess_info, times_left):
        # npc对应的飞行棋哪个包中(一共4个包)
        self.goods_position = goods_position
        # 飞行棋在物品栏的第几行(1-4)
        self.goods_position_x = goods_position_x
        # 飞行棋在物品栏包的垂直位置(1-6)
        self.goods_position_y = goods_position_y
        # 飞行棋在哪个地图,具体坐标是什么
        self.flight_chess_info = flight_chess_info
        # 飞行棋信息飞行棋所剩次数
        self.times_left = times_left
