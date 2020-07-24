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
        self.move_to(150, 290)
        self.click_left()

    def select_option(self, type, position):
        '''选择选项

        :param type:
        :param position:
        :return:
        '''
        y = 0
        if type == 0:
            y = 255
        elif type == 1:
            y = 290
        elif type == 2:
            y = 308
        self.move_to(150, y + ((position - 1) * 18))
        self.click_left()

    def open_inventory(self):
        """打开物品栏
        """
        self.move_to(527, 611)
        self.click_left()

    def select_inventory(self, position):
        """选择背包1还是背包2
        """
        if position == 1:
            self.move_to(760, 360)
        else:
            self.move_to(760, 360 + ((position - 1) * 51))
        self.click_left()

    def carry_store(self):
        """打开随身商店
        """
        # self.move_to(735, 555)
        self.move_to(650, 555)
        self.click_left()

    def carry_store_buy(self, gx, gy):
        """从随身商店购买商品
        """
        self.move_to(273, 175)
        self.click_left()
        horizontal_one = 273
        vertical_one = 175
        distance = 51
        horizontal_one = horizontal_one + ((gy - 1) * distance)
        vertical_one = vertical_one + ((gx - 1) * distance)
        self.move_to(horizontal_one, vertical_one)
        self.click_left()
        self.move_to(405, 500)
        self.click_left()
        self.move_to(563, 114)
        self.click_left()

    def select_goods(self, gx, gy):
        """选择指定位置的物品
        :param int gx: 水平位置(取值范围1-6).
        :param int gy: 垂直位置(取值范围1-4).
        """
        horizontal_one = 469
        vertical_one = 360
        distance = 51
        horizontal_one = horizontal_one + ((gy - 1) * distance)
        vertical_one = vertical_one + ((gx - 1) * distance)
        self.move_to(horizontal_one, vertical_one)
        self.click_right()

    def move_goods(self, gx, gy):
        """选择指定位置的物品
        :param int gx: 水平位置(取值范围1-6).
        :param int gy: 垂直位置(取值范围1-4).
        """
        horizontal_one = 469
        vertical_one = 360
        distance = 51
        horizontal_one = horizontal_one + ((gy - 1) * distance)
        vertical_one = vertical_one + ((gx - 1) * distance)
        self.move_to(horizontal_one, vertical_one)
        self.click_left()

    def submit_task(self, talk_type, position):
        '''提交任务

        :param self:
        :param int type: 根据对话长度点击不同的选线
        :param int position: 选择第几个个
        :return:
        '''
        if talk_type == 0:
            self.move_to(150, 255)
        elif talk_type == 1:
            self.move_to(150, 290 + ((position - 1) * 18))
        elif talk_type == 2:
            self.move_to(150, 308 + ((position - 1) * 18))
        self.click_left()
