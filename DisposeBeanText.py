import json

from DaHuaInterfaceUtil import file_path
from DisposeBean import DisposeBean, TalkBean

"""
在这里添加任务信息
"""
# list = []
# list.append(DisposeBean(1, '王秀才博学多才，代我问下他考研补？', 'wangxiucai.jpg', '王秀才', 530, 172, '长安城(199,72)').__dict__)
# list.append(DisposeBean(1, '听说疯牛怪，患有疯牛病，你给他送一个羚羊角过去探望一下。', 'fengniuguai.jpg', '疯牛怪', 100, 100, '狮驼岭(34,58)').__dict__)
# list.append(DisposeBean(1, '何小姐，说自己很喜欢萧举人，一直在等待他的表白', 'hexiaojie.jpg', '何小姐', 235, 225, '洛阳城(63,130)').__dict__)
# list.append(DisposeBean(1, '何小姐，说自己很喜欢萧举人，一直在等待他的表白', 'huqiaoer.jpg', '何小姐', 296, 175, '洛阳城(154,95)').__dict__)
# list.append(DisposeBean(1, '何小姐，说自己很喜欢萧举人，一直在等待他的表白', 'huanghuoniu.jpg', '何小姐', 285, 262, '洛阳城(256,13)').__dict__)
#
# list.append(DisposeBean(2, '何小姐，说自己很喜欢萧举人，一直在等待他的表白', 'meihuaxian.jpg', '何小姐', 300, 252, '长安东(64,26)').__dict__)
#
# list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番', 'shenling.jpg', '神灵', 558, 110, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番', 'shenling1.jpg', '神灵', 558, 110, '蟠桃园(81,85)').__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TaskProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)

# list = []
# list.append(FlightBean(1, 1, 1, '长安城(199,72)', 20).__dict__)
# list.append(FlightBean(1, 1, 2, '长安城(138,44)', 20).__dict__)
# list.append(FlightBean(1, 1, 3, '长安城(126,13)', 20).__dict__)
# list.append(FlightBean(1, 1, 4, '长安城(16,135)', 20).__dict__)
# list.append(FlightBean(1, 1, 5, '长安城(44,124)', 20).__dict__)
# list.append(FlightBean(1, 1, 6, '长安城(80,138)', 20).__dict__)
#
# list.append(FlightBean(1, 2, 1, '长安城(24,91)', 20).__dict__)
# list.append(FlightBean(1, 2, 2, '长安城(255,52)', 20).__dict__)
# list.append(FlightBean(1, 2, 3, '洛阳城(256,13)', 20).__dict__)
# list.append(FlightBean(1, 2, 4, '洛阳城(232,21)', 20).__dict__)
# list.append(FlightBean(1, 2, 5, '洛阳城(154,95)', 20).__dict__)
# list.append(FlightBean(1, 2, 6, '洛阳城(175,102)', 20).__dict__)
#
# list.append(FlightBean(1, 3, 1, '洛阳城(214,113)', 20).__dict__)
# list.append(FlightBean(1, 3, 2, '洛阳城(157,138)', 20).__dict__)
# list.append(FlightBean(1, 3, 3, '洛阳城(63,130)', 20).__dict__)
# list.append(FlightBean(1, 3, 4, '洛阳城(248,118)', 20).__dict__)
# list.append(FlightBean(1, 3, 5, '洛阳城(198,69)', 20).__dict__)
# list.append(FlightBean(1, 3, 6, '蟠桃园(15,49)', 20).__dict__)
#
# list.append(FlightBean(1, 4, 1, '蟠桃园(81,85)', 20).__dict__)
# list.append(FlightBean(1, 4, 2, '蟠桃园(39,68)', 20).__dict__)
# list.append(FlightBean(1, 4, 3, '东海渔村(30,17)', 20).__dict__)
# list.append(FlightBean(1, 4, 4, '东海渔村(43,52)', 20).__dict__)
# list.append(FlightBean(1, 4, 5, '长安东(34,36)', 20).__dict__)
# list.append(FlightBean(1, 4, 6, '长安东(64,26)', 20).__dict__)
#
# list.append(FlightBean(2, 1, 1, '长寿村(46,70)', 20).__dict__)
# list.append(FlightBean(2, 1, 2, '长寿村(14,145)', 20).__dict__)
# list.append(FlightBean(2, 1, 3, '地狱迷宫2(25,15)', 20).__dict__)
# list.append(FlightBean(2, 1, 4, '地狱迷宫4(6,19)', 20).__dict__)
# list.append(FlightBean(2, 1, 5, '五指山(165,49)', 20).__dict__)
# list.append(FlightBean(2, 1, 6, '五指山(21,43)', 20).__dict__)
#
# list.append(FlightBean(2, 2, 1, '普陀山(15,55)', 20).__dict__)
# list.append(FlightBean(2, 2, 2, '方寸山(21,23)', 20).__dict__)
# list.append(FlightBean(2, 2, 3, '玄空僧房(14,14)', 20).__dict__)
# list.append(FlightBean(2, 2, 4, '狮驼岭(34,58)', 20).__dict__)
#
# list.append(FlightBean(2, 3, 2, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 3, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 5, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 6, '备用棋', 99).__dict__)
#
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)

# list = []
# list.append(TalkBean(2, '这长安城中有一大雁塔，听说里面镇压了十万妖魔，要是没有两把刷子可别进去送死。', 'talk_2_1.jpg', ).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TalkProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)
