import json

from DaHuaInterfaceUtil import tian_path, file_path, huishou_path
from DisposeBean import FlightBean, TalkBean

"""
在这里添加任务信息
"""
# list = []
# list.append(DisposeBean(1, '王秀才博学多才，代我问下他考研补？', 'wangxiucai.jpg', '王秀才', 530, 172, '长安城(199,72)').__dict__)
# list.append(DisposeBean(1, '听说疯牛怪，患有疯牛病，你给他送一个羚羊角过去探望一下。', 'fengniuguai.jpg', '疯牛怪', 533, 332, '狮驼岭(34,58)').__dict__)
# list.append(DisposeBean(1, '何小姐，说自己很喜欢萧举人，一直在等待他的表白。', 'hexiaojie.jpg', '何小姐', 235, 225, '洛阳城(63,130)').__dict__)
# list.append(DisposeBean(1, '胡巧儿的杂技出神入化啊，你要不要去看看。', 'huqiaoer.jpg', '胡巧儿', 296, 175, '洛阳城(154,95)').__dict__)
# list.append(DisposeBean(1, '听说黄火牛前几天被人打了，你去看看他伤势如何。', 'huanghuoniu.jpg', '黄火牛', 285, 262, '洛阳城(256,13)').__dict__)
# list.append(DisposeBean(1, '天灯老人每当想去女儿就会哭啼不止，你去问候一下吧。', 'tiandenglaoren.jpg', '天灯老人', 279, 290, '长安城(80,138)').__dict__)
# list.append(DisposeBean(1, '长安的衙役因为最近站岗太郁闷，开导一下他。', 'yayi.jpg', '衙役', 305, 265, '长安城(126,13)').__dict__)
# list.append(DisposeBean(1, '渔村村长说统计民普，你去找他报个名吧。', 'yucuncunzhang.jpg', '渔村村长', 312, 283, '东海渔村(30,17)').__dict__)
# list.append(DisposeBean(1, '李老九说希望在有生之年见到大侠。你不妨去见见他吧。', 'lilaojiu.jpg', '李老九', 300, 266, '长安城(16,135)').__dict__)
# list.append(DisposeBean(1, '渔村的乞丐心里想念亲人，你去问候下给他点人情温暖。', 'qigai.jpg', '乞丐', 577, 180, '东海渔村(43,52)').__dict__)
# list.append(DisposeBean(1, '传闻袁天罡知道前生来世，又是可以去找到他。', 'yuantiangang.jpg', '袁天罡', 284, 270, '长安城(138,44)').__dict__)
# list.append(DisposeBean(1, '小黑说，想找个人聊聊天，你去陪陪她吧。', 'xiaohei.jpg', '小黑', 309, 419, '长寿村(14,145)').__dict__)
# list.append(DisposeBean(1, '听说玉狐仙说，你去查明情况。', 'yuhuxian.jpg', '玉狐仙', 378, 366, '普陀山(15,55)').__dict__)
# list.append(DisposeBean(1, '玄奘前些天嘱咐说有事找你，你赶快过去看看。', 'xuanzang.jpg', '玄奘', 442, 158, '玄空僧房(14,14)').__dict__)
# list.append(DisposeBean(1, '问问洛阳的胡大力打听下百晓生的下落。', 'hudali.jpg', '胡大力', 302, 316, '洛阳城(232,21)').__dict__)
# list.append(DisposeBean(1, '桃园土地，说最近郁闷想找你聊聊。', 'pantaoyuantudi.jpg', '桃园土地', 278, 224, '蟠桃园(15,49)').__dict__)
# list.append(DisposeBean(1, '陈老才，说他想传授你，生意经你赶快去吧。', 'chenlaocai.jpg', '陈老才', 341, 281, '长寿村(46,70)').__dict__)
# list.append(DisposeBean(1, '牛头，说今夜要勾老贾的魂魄，你速去阻止一下吧。', 'niutou.jpg', '牛头', 311, 275, '地狱迷宫2(25,15)').__dict__)
# list.append(DisposeBean(1, '老猴精年事已高身体抱恙，你带上旋复花去看看他吧。', 'laohoujing.jpg', '老猴精', 325, 279, '五指山(21,43)').__dict__)
# list.append(DisposeBean(1, '马面，说想让自己变帅气点，你去找他讨论下。', 'mamian.jpg', '马面', 88, 262, '地狱迷宫4(6,19)').__dict__)
# list.append(DisposeBean(1, '陈夫人说老贾喜欢他，可惜一直等不到老贾的表白，然后生气不见老贾。', 'chenfuren.jpg', '陈夫人', 325, 279, '长安城(44,124)').__dict__)
# list.append(DisposeBean(1, '萧举人，说自己很喜欢何小姐，但是苦于表白，你去看看吧。', 'xiaojuren.jpg', '萧举人', 560, 240, '洛阳城(63,130)').__dict__)
# list.append(DisposeBean(1, '顶天柱，说要向你请教如何训练铁砂掌，你不妨去看看', 'dingtianzhu.jpg', '顶天柱', 269, 265, '洛阳城(198,69)').__dict__)
# list.append(DisposeBean(1, '顶天柱前几天表演弄伤身体了，帮我送点金创药给他。', 'dingtianzhu1.jpg', '顶天柱', 269, 265, '洛阳城(198,69)').__dict__)
# list.append(DisposeBean(1, '何老才，在收集羚羊角，你买一个送给他吧。', 'helaocai.jpg', '何老才', 296, 256, '洛阳城(248,118)').__dict__)
# list.append(DisposeBean(1, '游方术士，说想收门徒苦于找不到徒弟，你去帮助他一下吧。', 'youfangshushi.jpg', '游方术士', 282, 247, '方寸山(21,23)').__dict__)
# list.append(DisposeBean(1, '五指山土，地说找你有点事情，你去看看吧。', 'wuzhishantudi.jpg', '五指山土地', 467, 270, '五指山(163,43)').__dict__)
# list.append(DisposeBean(1, '鲁大婶，最近很苦恼你去问问为何如此苦恼。', 'ludashen.jpg', '鲁大婶', 331, 213, '洛阳城(157,138)').__dict__)
# list.append(DisposeBean(1, '前几天洛阳桥发生挤压，游客受到了惊吓，你去看看那吧。', 'youke.jpg', '游客', 332, 235, '洛阳城(175,102)').__dict__)
# list.append(DisposeBean(1, '满堂春，在找亲父你有什么消息赶快告诉他吧。', 'mantangchun.jpg', '满堂春', 307, 261, '洛阳城(214,113)').__dict__)
#
# list.append(DisposeBean(2, '梅花仙，说自己想要个簪子，你买一个送给他吧。', 'meihuaxian.jpg', '梅花仙', 300, 252, '长安东(64,26)').__dict__)
# list.append(DisposeBean(2, '秦琼在找一件拿手的武器，你去买一把长枪送给他。', 'qinqiong.jpg', '秦琼', 559, 174, '长安城(255,52)').__dict__)
# list.append(DisposeBean(2, '老贾想学习武艺，一直头痛找不到铁拳套，你去买个送给他吧。', 'laojia.jpg', '老贾', 292, 255, '长安东(34,36)').__dict__)
# list.append(DisposeBean(2, '庞夫人前几天看上了一件布裙，你买个他当做礼物吧。', 'pangfuren.jpg', '庞夫人', 329, 270, '长安城(24,91)').__dict__)
# list.append(DisposeBean(2, '情花仙子的鞋子丢了，正为此事发愁呢，你去买双布鞋送给他。', 'qinghuaxianzi.jpg', '情花仙子', 210, 383, '东海渔村(43,52)').__dict__)
#
# list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番。', 'shenling.jpg', '神灵', 558, 110, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番。', 'shenling1.jpg', '神灵', 558, 110, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃女娲偷吃了蟠桃去教训他一番。', 'nvwa.jpg', '女娲', 172, 480, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃女娲偷吃了蟠桃去教训他一番。', 'nvwa1.jpg', '女娲', 172, 480, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃凤凰偷吃了蟠桃去教训他一番。', 'fenghuang.jpg', '凤凰', 228, 266, '蟠桃园(39,68)').__dict__)
# list.append(DisposeBean(3, '蟠桃凤凰偷吃了蟠桃去教训他一番。', 'fenghuang1.jpg', '凤凰', 228, 266, '蟠桃园(39,68)').__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TaskProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)

# list = []
# list.append(FlightBean(1, 1, 1, '长安城(199,72)', 15).__dict__)
# list.append(FlightBean(1, 1, 2, '长安城(138,44)', 10).__dict__)
# list.append(FlightBean(1, 1, 3, '长安城(126,13)', 83).__dict__)
# list.append(FlightBean(1, 1, 4, '长安城(16,135)', 95).__dict__)
# list.append(FlightBean(1, 1, 5, '长安城(44,124)', 90).__dict__)
# list.append(FlightBean(1, 1, 6, '长安城(80,138)', 14).__dict__)
#
# list.append(FlightBean(1, 2, 1, '长安城(24,91)', 18).__dict__)
# list.append(FlightBean(1, 2, 2, '长安城(255,52)', 87).__dict__)
# list.append(FlightBean(1, 2, 3, '洛阳城(256,13)', 10).__dict__)
# list.append(FlightBean(1, 2, 4, '洛阳城(232,21)', 18).__dict__)
# list.append(FlightBean(1, 2, 5, '洛阳城(154,95)', 95).__dict__)
# list.append(FlightBean(1, 2, 6, '洛阳城(175,102)', 91).__dict__)
#
# list.append(FlightBean(1, 3, 1, '洛阳城(214,113)', 9).__dict__)
# list.append(FlightBean(1, 3, 2, '洛阳城(157,138)', 90).__dict__)
# list.append(FlightBean(1, 3, 3, '洛阳城(63,130)', 30).__dict__)
# list.append(FlightBean(1, 3, 4, '洛阳城(248,118)', 17).__dict__)
# list.append(FlightBean(1, 3, 5, '洛阳城(198,69)', 93).__dict__)
# list.append(FlightBean(1, 3, 6, '蟠桃园(15,49)', 95).__dict__)
#
# list.append(FlightBean(1, 4, 1, '蟠桃园(81,85)', 99).__dict__)
# list.append(FlightBean(1, 4, 2, '蟠桃园(39,68)', 38).__dict__)
# list.append(FlightBean(1, 4, 3, '东海渔村(30,17)', 98).__dict__)
# list.append(FlightBean(1, 4, 4, '东海渔村(43,52)', 98).__dict__)
# list.append(FlightBean(1, 4, 5, '长安东(34,36)', 9).__dict__)
# list.append(FlightBean(1, 4, 6, '长安东(64,26)', 3).__dict__)
#
# list.append(FlightBean(2, 1, 1, '长寿村(46,70)', 9).__dict__)
# list.append(FlightBean(2, 1, 2, '长寿村(14,145)', 3).__dict__)
# list.append(FlightBean(2, 1, 3, '地狱迷宫2(25,15)', 18).__dict__)
# list.append(FlightBean(2, 1, 4, '地狱迷宫4(6,19)', 10).__dict__)
# list.append(FlightBean(2, 1, 5, '五指山(163,43)', 8).__dict__)
# list.append(FlightBean(2, 1, 6, '五指山(21,43)', 12).__dict__)
#
# list.append(FlightBean(2, 2, 1, '普陀山(15,55)', 1).__dict__)
# list.append(FlightBean(2, 2, 2, '方寸山(21,23)', 95).__dict__)
# list.append(FlightBean(2, 2, 3, '玄空僧房(14,14)', 8).__dict__)
# list.append(FlightBean(2, 2, 4, '狮驼岭(34,58)', 10).__dict__)
#
# list.append(FlightBean(2, 3, 2, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 3, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 5, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 6, '备用棋', 99).__dict__)
#
# list.append(FlightBean(2, 4, 1, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 2, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 3, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 5, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 6, '备用棋', 99).__dict__)
#
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)

# list = []
# list.append(TalkBean(2, '这长安城中有一大雁塔，听说里面镇压了十万妖魔，要是没有两把刷子可别进去送死。', 'talk_2_1.jpg', ).__dict__)
# list.append(TalkBean(2, '在我所知道的关于孙悟空的故事中，他在一万多年里持续与天地神佛为敌，这到底是为什么呢？究竟为了什么，他要破坏三界的平衡？', 'talk_2_2.jpg', ).__dict__)
# list.append(TalkBean(2, '我们狮驼岭有三位大王，大大王能吞十万天兵，二大王一身铜身铁臂，三大王搏风运雾，谁人能敌？', 'talk_2_3.jpg', ).__dict__)
# list.append(TalkBean(0, '', 'talk_0_1.jpg', ).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TalkProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)


# list = []
# list.append(FlightBean(1, 1, 1, '长安城(199,72)', 15).__dict__)
# list.append(FlightBean(1, 1, 2, '备用棋', 99).__dict__)
# list.append(FlightBean(1, 1, 3, '备用棋', 99).__dict__)
# list.append(FlightBean(1, 1, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(1, 1, 5, '备用棋', 99).__dict__)
#


# myClassReBuild = json.loads(read_ispose(file_path + 'FlightChessProfile.txt'))
# flight_chess_datas = []
# for letter in myClassReBuild:
#     flight_chess_datas.append(
#         FlightBean(letter['goods_position'], letter['goods_position_x'], letter['goods_position_y'],
#                    letter['flight_chess_info'], letter['times_left']))
# list = []
# for temp in flight_chess_datas:
#     list.append(temp.__dict__)
# list.append(FlightBean(2, 3, 5, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 6, '备用棋', 99).__dict__)
#
# list.append(FlightBean(2, 4, 1, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 2, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 3, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 5, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 4, 6, '备用棋', 99).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)


# 怀旧西游
# list = []
# # list.append(DisposeBean(1, '李老九说希望在有生之年见到大侠。你不妨去见见他吧。', 'lilaojiu.jpg', '李老九', 300, 266, '长安城(16,135)').__dict__)
# # list.append(DisposeBean(1, '陈夫人说老贾喜欢他，可惜一直等不到老贾的表白，然后生气不见老贾。', 'chenfuren.jpg', '陈夫人', 326, 282, '长安城(64,112)').__dict__)
# # list.append(DisposeBean(1, '听说黄火牛前几天被人打了，你去看看他伤势如何。', 'huanghuoniu.jpg', '黄火牛', 335, 278, '洛阳城(254,13)').__dict__)
# # list.append(DisposeBean(1, '满堂春，在找亲父你有什么消息赶快告诉他吧。', 'mantangchun.jpg', '满堂春', 337, 297, '洛阳城(213,112)').__dict__)
# # list.append(DisposeBean(1, '长安的衙役因为最近站岗太郁闷，开导一下他。', 'yayi.jpg', '衙役', 242, 306, '长安城(126,13)').__dict__)
# # list.append(DisposeBean(1, '天灯老人每当想去女儿就会哭啼不止，你去问候一下吧。', 'tiandenglaoren.jpg', '天灯老人', 338, 290, '长安城(79,138)').__dict__)
# # list.append(DisposeBean(1, '传闻袁天罡知道前生来世，又是可以去找到他。', 'yuantiangang.jpg', '袁天罡', 284, 270, '长安城(138,44)').__dict__)
# # list.append(DisposeBean(1, '问问洛阳的胡大力打听下百晓生的下落。', 'hudali.jpg', '胡大力', 334, 265, '洛阳城(231,22)').__dict__)
# # list.append(DisposeBean(1, '五指山土，地说找你有点事情，你去看看吧。', 'wuzhishantudi.jpg', '五指山土地', 321, 255, '五指山(167,43)').__dict__)
# # list.append(DisposeBean(1, '萧举人，说自己很喜欢何小姐，但是苦于表白，你去看看吧。', 'xiaojuren.jpg', '萧举人', 572, 240, '洛阳城(63,130)').__dict__)
# # list.append(DisposeBean(1, '小黑说，想找个人聊聊天，你去陪陪她吧。', 'xiaohei.jpg', '小黑', 339, 420, '长寿村(13,145)').__dict__)
# # list.append(DisposeBean(1, '桃园土地，说最近郁闷想找你聊聊。', 'pantaoyuantudi.jpg', '桃园土地', 304, 270, '蟠桃园(13,48)').__dict__)
# # list.append(DisposeBean(1, '何老才，在收集羚羊角，你买一个送给他吧。', 'helaocai.jpg', '何老才', 327, 260, '洛阳城(247,118)').__dict__)
# # list.append(DisposeBean(1, '听说玉狐仙说，你去查明情况。', 'yuhuxian.jpg', '玉狐仙', 384, 366, '普陀山(15,54)').__dict__)
# # list.append(DisposeBean(1, '渔村村长说统计民普，你去找他报个名吧。', 'yucuncunzhang.jpg', '渔村村长', 309, 271, '东海渔村(57,43)').__dict__)
#
# list.append(DisposeBean(1, '王秀才博学多才，代我问下他考研补？', 'wangxiucai.jpg', '王秀才', 530, 172, '长安城(199,72)').__dict__)
# list.append(DisposeBean(1, '听说疯牛怪，患有疯牛病，你给他送一个羚羊角过去探望一下。', 'fengniuguai.jpg', '疯牛怪', 533, 332, '狮驼岭(34,58)').__dict__)
# list.append(DisposeBean(1, '何小姐，说自己很喜欢萧举人，一直在等待他的表白。', 'hexiaojie.jpg', '何小姐', 235, 225, '洛阳城(63,130)').__dict__)
# list.append(DisposeBean(1, '胡巧儿的杂技出神入化啊，你要不要去看看。', 'huqiaoer.jpg', '胡巧儿', 296, 175, '洛阳城(154,95)').__dict__)
# list.append(DisposeBean(1, '渔村的乞丐心里想念亲人，你去问候下给他点人情温暖。', 'qigai.jpg', '乞丐', 577, 180, '东海渔村(43,52)').__dict__)
# list.append(DisposeBean(1, '玄奘前些天嘱咐说有事找你，你赶快过去看看。', 'xuanzang.jpg', '玄奘', 442, 158, '玄空僧房(14,14)').__dict__)
# list.append(DisposeBean(1, '陈老才，说他想传授你，生意经你赶快去吧。', 'chenlaocai.jpg', '陈老才', 341, 281, '长寿村(46,70)').__dict__)
# list.append(DisposeBean(1, '牛头，说今夜要勾老贾的魂魄，你速去阻止一下吧。', 'niutou.jpg', '牛头', 311, 275, '地狱迷宫2(25,15)').__dict__)
# list.append(DisposeBean(1, '老猴精年事已高身体抱恙，你带上旋复花去看看他吧。', 'laohoujing.jpg', '老猴精', 325, 279, '五指山(21,43)').__dict__)
# list.append(DisposeBean(1, '马面，说想让自己变帅气点，你去找他讨论下。', 'mamian.jpg', '马面', 88, 262, '地狱迷宫4(6,19)').__dict__)
# list.append(DisposeBean(1, '顶天柱，说要向你请教如何训练铁砂掌，你不妨去看看', 'dingtianzhu.jpg', '顶天柱', 269, 265, '洛阳城(198,69)').__dict__)
# list.append(DisposeBean(1, '顶天柱前几天表演弄伤身体了，帮我送点金创药给他。', 'dingtianzhu1.jpg', '顶天柱', 269, 265, '洛阳城(198,69)').__dict__)
# list.append(DisposeBean(1, '游方术士，说想收门徒苦于找不到徒弟，你去帮助他一下吧。', 'youfangshushi.jpg', '游方术士', 282, 247, '方寸山(21,23)').__dict__)
# list.append(DisposeBean(1, '鲁大婶，最近很苦恼你去问问为何如此苦恼。', 'ludashen.jpg', '鲁大婶', 331, 213, '洛阳城(157,138)').__dict__)
# list.append(DisposeBean(1, '前几天洛阳桥发生挤压，游客受到了惊吓，你去看看那吧。', 'youke.jpg', '游客', 332, 235, '洛阳城(175,102)').__dict__)
#
# # list.append(DisposeBean(2, '秦琼在找一件拿手的武器，你去买一把长枪送给他。', 'qinqiong.jpg', '秦琼', 336, 321, '长安城(262,48)').__dict__)
# # list.append(DisposeBean(2, '情花仙子的鞋子丢了，正为此事发愁呢，你去买双布鞋送给他。', 'qinghuaxianzi.jpg', '情花仙子', 435, 130, '东海渔村(27,93)').__dict__)
# # list.append(DisposeBean(2, '老贾想学习武艺，一直头痛找不到铁拳套，你去买个送给他吧。', 'laojia.jpg', '老贾', 331, 292, '长安东(45,36)').__dict__)
# # list.append(DisposeBean(2, '梅花仙，说自己想要个簪子，你买一个送给他吧。', 'meihuaxian.jpg', '梅花仙', 329, 302, '长安东(63,26)').__dict__)
#
# list.append(DisposeBean(2, '庞夫人前几天看上了一件布裙，你买个他当做礼物吧。', 'pangfuren.jpg', '庞夫人', 329, 270, '长安城(24,91)').__dict__)
#
# # list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番。', 'shenling.jpg', '神灵', 527, 110, '蟠桃园(82,85)').__dict__)
# # list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番。', 'shenling1.jpg', '神灵', 527, 110, '蟠桃园(82,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃女娲偷吃了蟠桃去教训他一番。', 'nvwa.jpg', '女娲', 172, 480, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃女娲偷吃了蟠桃去教训他一番。', 'nvwa1.jpg', '女娲', 172, 480, '蟠桃园(81,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃凤凰偷吃了蟠桃去教训他一番。', 'fenghuang.jpg', '凤凰', 248, 308, '蟠桃园(38,67)').__dict__)
# list.append(DisposeBean(3, '蟠桃凤凰偷吃了蟠桃去教训他一番。', 'fenghuang1.jpg', '凤凰', 248, 308, '蟠桃园(38,67)').__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TaskProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)

# list = []
# list.append(FlightBean(1, 1, 1, '长安城(199,72)', 991).__dict__)
# list.append(FlightBean(1, 1, 2, '长安城(138,44)', 60).__dict__)
# list.append(FlightBean(1, 1, 3, '长安城(126,13)', 68).__dict__)
# list.append(FlightBean(1, 1, 4, '长安城(16,135)', 50).__dict__)
# list.append(FlightBean(1, 1, 5, '长安城(64,112)', 960).__dict__)
# list.append(FlightBean(1, 1, 6, '长安城(79,138)', 959).__dict__)
#
# list.append(FlightBean(1, 2, 1, '长安城(24,91)', 61).__dict__)
# list.append(FlightBean(1, 2, 2, '长安城(262,48)', 68).__dict__)
# list.append(FlightBean(1, 2, 3, '洛阳城(254,13)', 957).__dict__)
# list.append(FlightBean(1, 2, 4, '洛阳城(231,22)', 920).__dict__)
# list.append(FlightBean(1, 2, 5, '洛阳城(153,92)', 970).__dict__)
# list.append(FlightBean(1, 2, 6, '洛阳城(174,101)', 975).__dict__)
#
# list.append(FlightBean(1, 3, 1, '洛阳城(213,112)', 962).__dict__)
# list.append(FlightBean(1, 3, 2, '洛阳城(157,136)', 960).__dict__)
# list.append(FlightBean(1, 3, 3, '洛阳城(63,130)', 931).__dict__)
# list.append(FlightBean(1, 3, 4, '洛阳城(247,118)', 61).__dict__)
# list.append(FlightBean(1, 3, 5, '洛阳城(196,69)', 40).__dict__)
# list.append(FlightBean(1, 3, 6, '蟠桃园(13,48)', 969).__dict__)
#
# list.append(FlightBean(1, 4, 1, '蟠桃园(82,85)', 773).__dict__)
# list.append(FlightBean(1, 4, 2, '蟠桃园(38,67)', 19).__dict__)
# list.append(FlightBean(1, 4, 3, '东海渔村(57,43)', 966).__dict__)
# list.append(FlightBean(1, 4, 4, '东海渔村(112,70)', 958).__dict__)
# list.append(FlightBean(1, 4, 5, '东海渔村(27,93)', 65).__dict__)
# list.append(FlightBean(1, 4, 6, '长安东(45,36)', 58).__dict__)
#
# list.append(FlightBean(2, 1, 1, '长安东(63,26)', 57).__dict__)
# list.append(FlightBean(2, 1, 2, '长寿村(47,70)', 961).__dict__)
# list.append(FlightBean(2, 1, 3, '长寿村(13,145)', 954).__dict__)
# list.append(FlightBean(2, 1, 4, '地狱迷宫2(24,15)', 956).__dict__)
# list.append(FlightBean(2, 1, 5, '地狱迷宫4(6,18)', 961).__dict__)
# list.append(FlightBean(2, 1, 6, '五指山(167,43)', 961).__dict__)
#
# list.append(FlightBean(2, 2, 1, '五指山(21,42)', 57).__dict__)
# list.append(FlightBean(2, 2, 2, '普陀山(15,54)', 965).__dict__)
# list.append(FlightBean(2, 2, 3, '方寸山(19,22)', 959).__dict__)
# list.append(FlightBean(2, 2, 4, '玄空僧房(14,14)', 963).__dict__)
# list.append(FlightBean(2, 2, 5, '狮驼岭(34,58)', 64).__dict__)
# list.append(FlightBean(2, 2, 6, '备用棋', 99).__dict__)
#
# list.append(FlightBean(2, 3, 1, '备用棋', 83).__dict__)
# list.append(FlightBean(2, 3, 2, '备用棋', 69).__dict__)
# list.append(FlightBean(2, 3, 3, '备用棋', 72).__dict__)
# list.append(FlightBean(2, 3, 4, '备用棋', 81).__dict__)
# list.append(FlightBean(2, 3, 5, '备用棋', 74).__dict__)
# list.append(FlightBean(2, 3, 6, '备用棋', 84).__dict__)
#
# list.append(FlightBean(2, 4, 1, '备用棋', 44).__dict__)
# list.append(FlightBean(2, 4, 2, '备用棋', 37).__dict__)
# list.append(FlightBean(2, 4, 3, '备用棋', 17).__dict__)
# list.append(FlightBean(2, 4, 4, '备用棋', 994).__dict__)
# list.append(FlightBean(2, 4, 5, '备用棋', 999).__dict__)
# list.append(FlightBean(2, 4, 6, '备用棋', 993).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)
#
# list = []
# list.append(TalkBean(2, '这长安城中有一大雁塔，听说里面镇压了十万妖魔，要是没有两把刷子可别进去送死。', 'talk_2_1.jpg', ).__dict__)
# list.append(TalkBean(2, '在我所知道的关于孙悟空的故事中，他在一万多年里持续与天地神佛为敌，这到底是为什么呢？究竟为了什么，他要破坏三界的平衡？', 'talk_2_2.jpg', ).__dict__)
# list.append(TalkBean(2, '我们狮驼岭有三位大王，大大王能吞十万天兵，二大王一身铜身铁臂，三大王搏风运雾，谁人能敌？', 'talk_2_3.jpg', ).__dict__)
# list.append(TalkBean(2, '铜钱拿着不太方便了，您能否给点银子？银子没有，能不能给点钞票啊？美元也可以啦', 'talk_2_4.jpg', ).__dict__)
# list.append(TalkBean(2, '欢迎您来到大话西游2世界，您可以邀请您的朋友一起回归', 'talk_2_5.jpg', ).__dict__)
# list.append(TalkBean(0, '', 'talk_0_1.jpg', ).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TalkProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)


# list = []
# list.append(FlightBean(1, 1, 1, '长安城(199,72)', 15).__dict__)
# list.append(FlightBean(1, 1, 2, '备用棋', 99).__dict__)
# list.append(FlightBean(1, 1, 3, '备用棋', 99).__dict__)
# list.append(FlightBean(1, 1, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(1, 1, 5, '备用棋', 99).__dict__)


# myClassReBuild = json.loads(read_ispose(file_path + 'FlightChessProfile.txt'))
# flight_chess_datas = []
# for letter in myClassReBuild:
#     flight_chess_datas.append(
#         FlightBean(letter['goods_position'], letter['goods_position_x'], letter['goods_position_y'],
#                    letter['flight_chess_info'], letter['times_left']))
# list = []
# for temp in flight_chess_datas:
#     list.append(temp.__dict__)
# # list.append(FlightBean(2, 3, 4, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 5, '备用棋', 99).__dict__)
# list.append(FlightBean(2, 3, 6, '备用棋', 99).__dict__)
#
# list.append(FlightBean(2, 4, 1, '备用棋', 99).__dict__)
# # list.append(FlightBean(2, 4, 2, '备用棋', 99).__dict__)
# # list.append(FlightBean(2, 4, 3, '备用棋', 99).__dict__)
# # list.append(FlightBean(2, 4, 4, '备用棋', 99).__dict__)
# # list.append(FlightBean(2, 4, 5, '备用棋', 99).__dict__)
# # list.append(FlightBean(2, 4, 6, '备用棋', 99).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)


# list = []
# list.append(DisposeBean(1, '李老九说希望在有生之年见到大侠。你不妨去见见他吧。', 'lilaojiu.jpg', '李老九', 310, 280, '长安城(16,135)').__dict__)
# list.append(DisposeBean(1, '陈夫人说老贾喜欢他，可惜一直等不到老贾的表白，然后生气不见老贾。', 'chenfuren.jpg', '陈夫人', 326, 282, '长安城(64,112)').__dict__)
# list.append(DisposeBean(1, '听说黄火牛前几天被人打了，你去看看他伤势如何。', 'huanghuoniu.jpg', '黄火牛', 335, 278, '洛阳城(254,13)').__dict__)
# list.append(DisposeBean(1, '满堂春，在找亲父你有什么消息赶快告诉他吧。', 'mantangchun.jpg', '满堂春', 337, 297, '洛阳城(213,112)').__dict__)
# list.append(DisposeBean(1, '长安的衙役因为最近站岗太郁闷，开导一下他。', 'yayi.jpg', '衙役', 242, 306, '长安城(126,13)').__dict__)
# list.append(DisposeBean(1, '天灯老人每当想去女儿就会哭啼不止，你去问候一下吧。', 'tiandenglaoren.jpg', '天灯老人', 338, 290, '长安城(79,138)').__dict__)
# list.append(DisposeBean(1, '传闻袁天罡知道前生来世，又是可以去找到他。', 'yuantiangang.jpg', '袁天罡', 284, 270, '长安城(138,44)').__dict__)
# list.append(DisposeBean(1, '问问洛阳的胡大力打听下百晓生的下落。', 'hudali.jpg', '胡大力', 334, 265, '洛阳城(231,22)').__dict__)
# list.append(DisposeBean(1, '五指山土，地说找你有点事情，你去看看吧。', 'wuzhishantudi.jpg', '五指山土地', 321, 255, '五指山(167,43)').__dict__)
# list.append(DisposeBean(1, '萧举人，说自己很喜欢何小姐，但是苦于表白，你去看看吧。', 'xiaojuren.jpg', '萧举人', 572, 240, '洛阳城(63,130)').__dict__)
# list.append(DisposeBean(1, '小黑说，想找个人聊聊天，你去陪陪她吧。', 'xiaohei.jpg', '小黑', 339, 420, '长寿村(13,145)').__dict__)
# list.append(DisposeBean(1, '桃园土地，说最近郁闷想找你聊聊。', 'pantaoyuantudi.jpg', '桃园土地', 304, 270, '蟠桃园(13,48)').__dict__)
# list.append(DisposeBean(1, '何老才，在收集羚羊角，你买一个送给他吧。', 'helaocai.jpg', '何老才', 327, 260, '洛阳城(247,118)').__dict__)
# list.append(DisposeBean(1, '听说玉狐仙说，你去查明情况。', 'yuhuxian.jpg', '玉狐仙', 384, 367, '普陀山(15,54)').__dict__)
# list.append(DisposeBean(1, '渔村村长说统计民普，你去找他报个名吧。', 'yucuncunzhang.jpg', '渔村村长', 309, 271, '东海渔村(57,43)').__dict__)
# list.append(DisposeBean(1, '王秀才博学多才，代我问下他考研补？', 'wangxiucai.jpg', '王秀才', 532, 196, '长安城(199,72)').__dict__)
# list.append(DisposeBean(1, '渔村的乞丐心里想念亲人，你去问候下给他点人情温暖。', 'qigai.jpg', '乞丐', 336, 270, '东海渔村(112,70)').__dict__)
# list.append(DisposeBean(1, '何小姐，说自己很喜欢萧举人，一直在等待他的表白。', 'hexiaojie.jpg', '何小姐', 247, 225, '洛阳城(63,130)').__dict__)
# list.append(DisposeBean(1, '老猴精年事已高身体抱恙，你带上旋复花去看看他吧。', 'laohoujing.jpg', '老猴精', 328, 300, '五指山(21,42)').__dict__)
# list.append(DisposeBean(1, '陈老才，说他想传授你，生意经你赶快去吧。', 'chenlaocai.jpg', '陈老才', 338, 296, '长寿村(47,70)').__dict__)
# list.append(DisposeBean(1, '鲁大婶，最近很苦恼你去问问为何如此苦恼。', 'ludashen.jpg', '鲁大婶', 320, 265, '洛阳城(157,136)').__dict__)
# list.append(DisposeBean(1, '听说疯牛怪，患有疯牛病，你给他送一个羚羊角过去探望一下。', 'fengniuguai.jpg', '疯牛怪', 533, 332, '狮驼岭(34,58)').__dict__)
# list.append(DisposeBean(1, '顶天柱，说要向你请教如何训练铁砂掌，你不妨去看看', 'dingtianzhu.jpg', '顶天柱', 328, 278, '洛阳城(196,69)').__dict__)
# list.append(DisposeBean(1, '游方术士，说想收门徒苦于找不到徒弟，你去帮助他一下吧。', 'youfangshushi.jpg', '游方术士', 333, 273, '方寸山(19,22)').__dict__)
# list.append(DisposeBean(1, '顶天柱前几天表演弄伤身体了，帮我送点金创药给他。', 'dingtianzhu1.jpg', '顶天柱', 328, 278, '洛阳城(196,69)').__dict__)
# list.append(DisposeBean(1, '玄奘前些天嘱咐说有事找你，你赶快过去看看。', 'xuanzang.jpg', '玄奘', 442, 158, '玄空僧房(14,14)').__dict__)
# list.append(DisposeBean(1, '牛头，说今夜要勾老贾的魂魄，你速去阻止一下吧。', 'niutou.jpg', '牛头', 330, 278, '地狱迷宫2(24,15)').__dict__)
# list.append(DisposeBean(1, '胡巧儿的杂技出神入化啊，你要不要去看看。', 'huqiaoer.jpg', '胡巧儿', 338, 260, '洛阳城(153,92)').__dict__)
# list.append(DisposeBean(1, '前几天洛阳桥发生挤压，游客受到了惊吓，你去看看那吧。', 'youke.jpg', '游客', 333, 257, '洛阳城(174,101)').__dict__)
# list.append(DisposeBean(1, '马面，说想让自己变帅气点，你去找他讨论下。', 'mamian.jpg', '马面', 88, 269, '地狱迷宫4(6,18)').__dict__)
#
# list.append(DisposeBean(2, '秦琼在找一件拿手的武器，你去买一把长枪送给他。', 'qinqiong.jpg', '秦琼', 336, 321, '长安城(262,48)').__dict__)
# list.append(DisposeBean(2, '情花仙子的鞋子丢了，正为此事发愁呢，你去买双布鞋送给他。', 'qinghuaxianzi.jpg', '情花仙子', 435, 130, '东海渔村(27,93)').__dict__)
# list.append(DisposeBean(2, '老贾想学习武艺，一直头痛找不到铁拳套，你去买个送给他吧。', 'laojia.jpg', '老贾', 331, 292, '长安东(45,36)').__dict__)
# list.append(DisposeBean(2, '梅花仙，说自己想要个簪子，你买一个送给他吧。', 'meihuaxian.jpg', '梅花仙', 329, 302, '长安东(63,26)').__dict__)
# list.append(DisposeBean(2, '庞夫人前几天看上了一件布裙，你买个他当做礼物吧。', 'pangfuren.jpg', '庞夫人', 329, 278, '长安城(24,91)').__dict__)
#
# list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番。', 'shenling.jpg', '神灵', 527, 110, '蟠桃园(82,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃神灵偷吃了蟠桃去教训他一番。', 'shenling1.jpg', '神灵', 527, 110, '蟠桃园(82,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃凤凰偷吃了蟠桃去教训他一番。', 'fenghuang.jpg', '凤凰', 248, 307, '蟠桃园(38,67)').__dict__)
# list.append(DisposeBean(3, '蟠桃凤凰偷吃了蟠桃去教训他一番。', 'fenghuang1.jpg', '凤凰', 248, 307, '蟠桃园(38,67)').__dict__)
# list.append(DisposeBean(3, '蟠桃女娲偷吃了蟠桃去教训他一番。', 'nvwa.jpg', '女娲', 142, 480, '蟠桃园(82,85)').__dict__)
# list.append(DisposeBean(3, '蟠桃女娲偷吃了蟠桃去教训他一番。', 'nvwa1.jpg', '女娲', 142, 480, '蟠桃园(82,85)').__dict__)
#
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(file_path + 'TaskProfile.txt', 'w', encoding='utf-8') as f:
#     f.write(str)

# 做天
# list = []
# list.append(FlightBean(1, 1, 1, '李靖', 99).__dict__)
# list.append(FlightBean(1, 1, 2, '三头魔王', 99).__dict__)
# list.append(FlightBean(1, 1, 3, '黑山妖王', 99).__dict__)
# list.append(FlightBean(1, 1, 4, '蓝色妖王', 99).__dict__)
# list.append(FlightBean(1, 1, 5, '万年妖王', 99).__dict__)
# list.append(FlightBean(1, 2, 1, '石破烂', 99).__dict__)
# str = json.dumps(list).encode('utf-8').decode('unicode_escape')
# with open(tian_path + 'ZuoTianFlightChess.txt', 'w', encoding='utf-8') as f:
#     f.write(str)


list = []
list.append(TalkBean(1, '亲密丹', 'qinmidan11.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan12.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan13.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan14.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan15.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan16.jpg', ).__dict__)

list.append(TalkBean(1, '亲密丹', 'qinmidan21.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan22.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan23.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan24.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan25.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan26.jpg', ).__dict__)

list.append(TalkBean(1, '亲密丹', 'qinmidan31.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan32.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan33.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan34.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan35.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan36.jpg', ).__dict__)

list.append(TalkBean(1, '亲密丹', 'qinmidan41.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan42.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan43.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan44.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan45.jpg', ).__dict__)
list.append(TalkBean(1, '亲密丹', 'qinmidan46.jpg', ).__dict__)

list.append(TalkBean(1, '血玲珑', 'xuelinglong11.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong12.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong13.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong14.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong15.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong16.jpg', ).__dict__)

list.append(TalkBean(1, '血玲珑', 'xuelinglong21.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong22.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong23.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong24.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong25.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong26.jpg', ).__dict__)

list.append(TalkBean(1, '血玲珑', 'xuelinglong31.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong32.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong33.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong34.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong35.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong36.jpg', ).__dict__)

list.append(TalkBean(1, '血玲珑', 'xuelinglong41.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong42.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong43.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong44.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong45.jpg', ).__dict__)
list.append(TalkBean(1, '血玲珑', 'xuelinglong46.jpg', ).__dict__)

list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu11.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu12.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu13.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu14.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu15.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu16.jpg', ).__dict__)

list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu21.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu22.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu23.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu24.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu25.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu26.jpg', ).__dict__)

list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu31.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu32.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu33.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu34.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu35.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu36.jpg', ).__dict__)

list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu41.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu42.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu43.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu44.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu45.jpg', ).__dict__)
list.append(TalkBean(1, '九彩云龙珠', 'jiucaiyunlongzhu46.jpg', ).__dict__)

list.append(TalkBean(1, '内丹精华', 'neidanjinghua11.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua12.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua13.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua14.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua15.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua16.jpg', ).__dict__)

list.append(TalkBean(1, '内丹精华', 'neidanjinghua21.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua22.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua23.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua24.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua25.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua26.jpg', ).__dict__)

list.append(TalkBean(1, '内丹精华', 'neidanjinghua31.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua32.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua33.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua34.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua35.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua36.jpg', ).__dict__)

list.append(TalkBean(1, '内丹精华', 'neidanjinghua41.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua42.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua43.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua44.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua45.jpg', ).__dict__)
list.append(TalkBean(1, '内丹精华', 'neidanjinghua46.jpg', ).__dict__)

list.append(TalkBean(1, '千年寒铁', 'qiannianhantie11.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie12.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie13.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie14.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie15.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie16.jpg', ).__dict__)

list.append(TalkBean(1, '千年寒铁', 'qiannianhantie21.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie22.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie23.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie24.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie25.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie26.jpg', ).__dict__)

list.append(TalkBean(1, '千年寒铁', 'qiannianhantie31.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie32.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie33.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie34.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie35.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie36.jpg', ).__dict__)

list.append(TalkBean(1, '千年寒铁', 'qiannianhantie41.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie42.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie43.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie44.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie45.jpg', ).__dict__)
list.append(TalkBean(1, '千年寒铁', 'qiannianhantie46.jpg', ).__dict__)

list.append(TalkBean(1, '天外飞石', 'tianwaifeishi11.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi12.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi13.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi14.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi15.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi16.jpg', ).__dict__)

list.append(TalkBean(1, '天外飞石', 'tianwaifeishi21.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi22.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi23.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi24.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi25.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi26.jpg', ).__dict__)

list.append(TalkBean(1, '天外飞石', 'tianwaifeishi31.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi32.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi33.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi34.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi35.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi36.jpg', ).__dict__)

list.append(TalkBean(1, '天外飞石', 'tianwaifeishi41.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi42.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi43.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi44.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi45.jpg', ).__dict__)
list.append(TalkBean(1, '天外飞石', 'tianwaifeishi46.jpg', ).__dict__)

list.append(TalkBean(1, '盘古精铁', 'pangujingtie11.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie12.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie13.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie14.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie15.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie16.jpg', ).__dict__)

list.append(TalkBean(1, '盘古精铁', 'pangujingtie21.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie22.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie23.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie24.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie25.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie26.jpg', ).__dict__)

list.append(TalkBean(1, '盘古精铁', 'pangujingtie31.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie32.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie33.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie34.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie35.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie36.jpg', ).__dict__)

list.append(TalkBean(1, '盘古精铁', 'pangujingtie41.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie42.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie43.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie44.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie45.jpg', ).__dict__)
list.append(TalkBean(1, '盘古精铁', 'pangujingtie46.jpg', ).__dict__)

str = json.dumps(list).encode('utf-8').decode('unicode_escape')
with open(huishou_path + 'KeHuiShouProfile.txt', 'w', encoding='utf-8') as f:
    f.write(str)
