from DisposeBean import DisposeBean, FlightBean
import json

"""
在这里添加任务信息
"""
list = []
# list.append(
#     DisposeBean(1, '王秀才博学多才,代我问下他考研不?', 'wangxiucai.jpg', '王秀才', 2, 1, 1, 558, 110,
#                 199, 72, 85).__dict__)
# list.append(
#     DisposeBean(2, '顶天柱前几天表演弄伤身体了,帮我送点金疮药给他', 'dingtianzhu2.jpg', '顶天柱', 2, 1, 5, 270, 265,
#                 198, 69, 62).__dict__)
# list.append(
#     DisposeBean(1, '小黑', 'shenling.jpg', '小黑', 1, 4, 4, 310, 420,
#                 14, 145, 85).__dict__)
# list.append(
#     DisposeBean(2, '听说疯牛怪,患有疯牛病,你给他送一个羚羊角过去探望一下', 'fengniuguai.jpg', '疯牛怪', 2, 2, 3, 533, 330,
#                 34, 58, 77).__dict__)


list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番', 'shenling.jpg', '神灵', 558, 110, '蟠桃园后,12,15').__dict__)

str = json.dumps(list).encode('utf-8').decode('unicode_escape')
with open('E://Dahua/TaskProfile.txt', 'w', encoding='utf-8') as f:
    f.write(str)


# list.append(FlightBean(1, 1, 1, '长安城(100,100)', 58).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open('E://Dahua/FlightChessProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)
