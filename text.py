import json
import time

import cv2
from playsound import playsound

from DaHuaInterfaceUtil import file_path
from DisposeBean import DisposeBean, FlightBean, TalkBean
from DisposeUtil import read_ispose
from MouseUtil import MouseUtil
from PictureUtil import screenshot, dHash, cmpHash
# 1初始化读取配置文件
# 200环任务数据
from TaskUtil import task_one, task_two, task_three

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
img1 = cv2.imread(file_path + 'heiping.jpg')
hashHeiPing = dHash(img1)
mouse = MouseUtil()
# 当前任务
current_coordinate = ''
# 相似度
con = 100
# 筛选出来的最终结果
current_task = ''
retryNum = 3
isFirst = 1
while True:
    mouse.move_to(400, 40)
    time.sleep(2)
    screenshot(140, 240, 450, 30, 'temp.jpg')
    img1 = cv2.imread('temp.jpg')
    hash1 = dHash(img1)
    if hashHeiPing == hash1:
        time.sleep(2)
        retryNum = retryNum - 1
        screenshot(140, 240, 450, 30, 'temp.jpg')
        img1 = cv2.imread('temp.jpg')
        hash1 = dHash(img1)
        if retryNum == 0:
            break
    for temp_task in task_datas:
        n = cmpHash(hash1, temp_task.imgHash)
        if n < con:
            con = n
            current_task = temp_task
    if current_task.task_type == 3:
        con = 100
        screenshot(174, 248, 29, 16, 'temp.jpg')
        img1 = cv2.imread('temp.jpg')
        hash1 = dHash(img1)
        for temp_task in task_datas:
            n = cmpHash(hash1, temp_task.imgHash)
            if n < con:
                con = n
                current_task = temp_task
    if con > 3:
        list = []
        for i in flight_chess_datas:
            list.append(i.__dict__)
        str = json.dumps(list).encode('utf-8').decode('unicode_escape')
        with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
            f.write(str)
        current_coordinate = ''
        print('没有找到对应任务')
        playsound("123.mp3")
        break
    else:
        mouse.receive_task()
        print(current_task.task_describe)
        if current_task.task_type == 1:
            current_coordinate = task_one(current_task, flight_chess_datas, talk_datas, current_coordinate)
        elif current_task.task_type == 2:
            current_coordinate = task_two(current_task, flight_chess_datas, talk_datas, current_coordinate)
        elif current_task.task_type == 3:
            if isFirst == 1:
                current_coordinate = task_three(current_task, flight_chess_datas, current_coordinate, 1)
                isFirst = 2
            else:
                current_coordinate = task_three(current_task, flight_chess_datas, current_coordinate, 2)
    con = 100
    retryNum = 3
