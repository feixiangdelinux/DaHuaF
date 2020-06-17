import json

import cv2

from DaHuaInterfaceUtil import file_path
from DisposeBean import DisposeBean, FlightBean, TalkBean
from DisposeUtil import read_ispose
from MouseUtil import MouseUtil
from PictureUtil import screenshot, dHash, cmpHash
from TaskUtil import task_one, task_three, task_two

# 1初始化读取配置文件
# 200环任务数据
myClassReBuild = json.loads(read_ispose(file_path + 'TaskProfile.txt'))
task_datas = []
for letter in myClassReBuild:
    task_datas.append(
        DisposeBean(letter['task_type'], letter['task_describe'], letter['task_picture'], letter['npc_name'],
                    letter['window_location_x'], letter['window_location_y'], letter['flight_chess_info']))
# 飞行棋数据
myClassReBuild = json.loads(read_ispose(file_path + 'FlightChessProfile.txt'))
flight_chess_datas = []
for letter in myClassReBuild:
    flight_chess_datas.append(
        FlightBean(letter['goods_position'], letter['goods_position_x'], letter['goods_position_y'],
                   letter['flight_chess_info'], letter['times_left']))
# npc对话数据
myClassReBuild = json.loads(read_ispose(file_path + 'TalkProfile.txt'))
talk_datas = []
for letter in myClassReBuild:
    talk_datas.append(TalkBean(letter['talk_type'], letter['talk_describe'], letter['talk_picture']))
mouse = MouseUtil()
# 当前任务
current_coordinate = ''
# 相似度
con = 100
# 筛选出来的最终结果
current_task = ''

# 2截图
screenshot(140, 240, 450, 30, 'temp.jpg')
img1 = cv2.imread('temp.jpg')
hash1 = dHash(img1)
# 2根据当前截图和图片库中所有的图片进行匹配
# 3选取相似度最小的那张图片作为最终结果
# 4根据最终筛选的图片,生成当前任务
for temp_task in task_datas:
    n = cmpHash(hash1, temp_task.imgHash)
    if n < con:
        con = n
        current_task = temp_task
if current_task.task_type == 3:
    screenshot(174, 248, 29, 16, 'temp.jpg')
    img1 = cv2.imread('temp.jpg')
    hash1 = dHash(img1)
    for temp_task in task_datas:
        n = cmpHash(hash1, temp_task.imgHash)
        if n < con:
            con = n
            current_task = temp_task
if con > 3:
    current_coordinate = ''
    print('没有找到对应任务')
else:
    # 5操作鼠标领取任务
    mouse.receive_task()
    # 执行任务
    if current_task.task_type == 1:
        print('执行任务1')
        current_coordinate = task_one(current_task, flight_chess_datas, talk_datas, current_coordinate)
    elif current_task.task_type == 2:
        print('执行任务2')
        current_coordinate = task_two(current_task, flight_chess_datas, talk_datas, current_coordinate)
    elif current_task.task_type == 3:
        print('执行任务3')
        current_coordinate = task_three(current_task, flight_chess_datas, current_coordinate)



# while True:
#     # 2截图
#     screenshot(140, 240, 450, 30, 'temp.jpg')
#     img1 = cv2.imread('temp.jpg')
#     hash1 = dHash(img1)
#     # 2根据当前截图和图片库中所有的图片进行匹配
#     # 3选取相似度最小的那张图片作为最终结果
#     # 4根据最终筛选的图片,生成当前任务
#     for temp_task in task_datas:
#         n = cmpHash(hash1, temp_task.imgHash)
#         if n < con:
#             con = n
#             current_task = temp_task
#     if current_task.task_type == 3:
#         screenshot(140, 240, 450, 30, 'temp.jpg')
#         img1 = cv2.imread('temp.jpg')
#         hash1 = dHash(img1)
#         for temp_task in task_datas:
#             n = cmpHash(hash1, temp_task.imgHash)
#             if n < con:
#                 con = n
#                 current_task = temp_task
#     if con > 3:
#         current_coordinate = ''
#         break
#     else:
#         # 5操作鼠标领取任务
#         MouseUtil.receive_task()
#         # 执行任务
#         if current_task.task_type == 1:
#             current_coordinate = task_one(current_task, flight_chess_datas, talk_datas, current_coordinate)
#         elif current_task.task_type == 2:
#             current_coordinate = task_two(current_task, flight_chess_datas, talk_datas, current_coordinate)
#         elif current_task.task_type == 3:
#             current_coordinate = task_three(current_task, flight_chess_datas, current_coordinate)