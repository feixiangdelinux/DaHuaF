import time

from pynput.mouse import Button, Controller


class MouseUtil:
    """大话西游鼠标操作的工具类
    包含各种鼠标点击，任务领取，物品使用等功能
    1左键点击npc
    2截图
    3领取任务
    4打开物品栏
    5选择背包1还是背包2
    6移动到对应的物品栏位置，右键使用物品
    7确定（3领取任务）

    """
    mouse = Controller()

    def move_to(self, dx, dy):
        """鼠标移动到某一位置

        :param int dx: 水平位置.

        :param int dy: 垂直位置.
        """
        time.sleep(1)
        self.mouse.position = (dx, dy)

    def click_left(self):
        """点击鼠标左键(一次)
        """
        time.sleep(1)
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)

    def click_right(self):
        """点击鼠标右键(一次)
        """
        time.sleep(1)
        self.mouse.press(Button.right)
        self.mouse.release(Button.right)

    def click_npc(self, dx, dy):
        """左键点击npc

        :param int dx: 水平位置.

        :param int dy: 垂直位置.
        """
        self.move_to(dx, dy)
        self.click_left()

    def receive_task(self):
        """领取任务
        """
        self.move_to(165, 263)
        self.click_left()

    def open_inventory(self):
        """打开物品栏
        """
        self.move_to(523, 615)
        self.click_left()

    def select_inventory(self, position):
        """选择背包1还是背包2
        """
        if position == 1:
            self.move_to(760, 360)
        else:
            self.move_to(760, 360 + ((position - 1) * 51))
        self.click_left()

    def select_goods(self, y, x):
        """右键使用指定位置的物品,比如飞行棋
        :param int y: 水平位置(取值范围1-6).
        :param int x: 垂直位置(取值范围1-4).
        """
        horizontal_one = 471
        vertical_one = 366
        distance = 51
        horizontal_one = horizontal_one + ((x - 1) * distance)
        vertical_one = vertical_one + ((y - 1) * distance)
        self.move_to(horizontal_one, vertical_one)
        self.click_right()

    def move_goods(self, y, x):
        """左键选择指定位置的物品
        :param int y: 水平位置(取值范围1-6).
        :param int x: 垂直位置(取值范围1-4).
        """
        horizontal_one = 471
        vertical_one = 366
        distance = 51
        horizontal_one = horizontal_one + ((y - 1) * distance)
        vertical_one = vertical_one + ((x - 1) * distance)
        self.move_to(horizontal_one, vertical_one)
        self.click_left()

    def buy_grocery(self, y, x):
        '''
        杂货店购买物品
        :param y: 第几行
        :param x: 第几个
        :return:
        '''
        # 点击npc
        MouseUtil().move_to(585, 400)
        MouseUtil().click_left()
        # 点击第一个购买物品
        MouseUtil().receive_task()
        # 鼠标移动到对应的飞行棋上面
        MouseUtil().move_to(229 + (51 * x), 131 + (51 * y))
        MouseUtil().click_left()
        # 购买
        MouseUtil().move_to(405, 507)
        MouseUtil().click_left()
        # 关闭
        MouseUtil().move_to(568, 120)
        MouseUtil().click_left()

    def move_goods_two(self, start_y, start_x, end_y, end_x):
        '''
        把物品栏里指定位置的物品start_x,start_y移动到另一个位置end_x,end_y
        :param start_y: 起始物品在第几行
        :param start_x: 起始物品是第几个
        :param end_y: 最终移动位置在第几行
        :param end_x: 最终移动位置是第几个
        :return:
        '''
        # 选取备用棋
        MouseUtil().move_goods(start_x, start_y)
        # 移动到空出的位置
        MouseUtil().move_goods(end_x, end_y)

    def replenish_piece(self, spare_y, spare_x, end_y, end_x):
        '''
        补棋,当前的棋子如果用完,把备用棋补充进来,并去商店补充备用棋
        :param spare_y: 备用棋在第几行
        :param spare_x: 备用棋是第几个
        :param end_y: 消失的棋子在第几行
        :param end_x: 消失的棋子是第几个
        :return:
        '''
        MouseUtil().move_goods_two(spare_y, spare_x, end_y, end_x)
        # 做棋
        MouseUtil().click_right()
        # 使用飞行棋飞到杂货店
        MouseUtil().select_goods(2, 1)
        MouseUtil().receive_task()
        # 关闭物品栏
        MouseUtil().open_inventory()
        # 购买第一个物品
        MouseUtil().buy_grocery(1, 1)
        # 关闭物品栏
        MouseUtil().open_inventory()

    def fly_destination(self, y, x):
        '''
        使用物品栏指定位置的飞行棋飞到目的地
        :param y: 飞行棋所在第几行
        :param x: 飞行棋是第几个
        :return:
        '''
        MouseUtil().select_goods(y, x)
        MouseUtil().receive_task()
