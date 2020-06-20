import json

import cv2

from DaHuaInterfaceUtil import file_path
from DisposeBean import TalkBean
from DisposeBeanText import myClassReBuild
from DisposeUtil import read_ispose
from TaskUtil import complete_task
# npc对话数据
myClassReBuild = json.loads(read_ispose(file_path + 'TalkProfile.txt'))

talk_datas = []
for letter in myClassReBuild:
    talk_datas.append(TalkBean(letter['talk_type'], letter['talk_describe'], letter['talk_picture']))
img1 = cv2.imread(file_path + 'heiping.jpg')

complete_task(talk_datas)