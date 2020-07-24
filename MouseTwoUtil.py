import time

from pynput.mouse import Button, Controller


class MouseTwoUtil:
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

    def drag_window(self, startx, starty, endx, endy):
        """
        拖动窗口到指定位置
        :param startx: 起点
        :param starty: 起点
        :param endx: 终点
        :param endy: 终点
        :return:
        """
        time.sleep(1)
        self.mouse.position = (startx, starty)
        self.mouse.press(Button.left)
        self.mouse.position = (endx, endy)
        self.mouse.release(Button.left)

    def click_npc(self, dx, dy):
        """左键点击npc

        :param int dx: 水平位置.

        :param int dy: 垂直位置.
        """
        self.move_to(dx, dy)
        self.click_left()

    def click_function(self, position):
        """
        左键点击下方的功能图标(养育，道具栏，组队等)
        :param position: 位置1是养育，位置2是道具栏，以此类推
        :return:
        """
        self.move_to(position * 29 + 693, 711)
        self.click_left()

    def select_goods(self, gx, gy):
        """选择指定位置的物品
        :param int gx: 第几行(取值范围1-4).
        :param int gy: 第几个(取值范围1-6).
        """
        self.move_to(gy * 50.5 + 896, gx * 50.5 + 362)

    def select_option(self, position):
        """
        选择对话框中指定选项
        :param position: 第几个选项
        :return:
        """
        self.move_to(390, position * 18 + 323)
        self.click_left()

    def select_prop_bottom(self, position):
        """
        点击道具栏底部按钮
        :param position: 第几个按钮
        :return:
        """
        self.click_function(2)
        self.move_to(position * 88 + 863, 610)
        self.click_left()

    def buy_prop(self, gx, gy):
        """
        从随身商店购买对应坐标的物品
        :param gx:
        :param gy:
        :return:
        """
        self.move_to(1 * 50.5 + 463, 1 * 50.5 + 177)
        self.click_left()
        self.move_to(gy * 50.5 + 463, gx * 50.5 + 177)
        self.click_left()
        self.move_to(640, 555)
        self.click_left()
        self.move_to(800, 165)
        self.click_left()
