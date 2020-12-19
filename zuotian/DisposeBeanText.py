import json

from zuotian.DisposeBean import FlightBean

file_path = 'E://Dahua/'
list = []
list.append(FlightBean(1, 1, 1, '天宫(37,33)', 30).__dict__)
list.append(FlightBean(1, 2, 1, '御马监(10,35)', 30).__dict__)
list.append(FlightBean(1, 3, 1, '御马监(100,10)', 30).__dict__)
list.append(FlightBean(1, 4, 1, '御马监(105,45)', 30).__dict__)
list.append(FlightBean(1, 5, 1, '御马监(110,100)', 30).__dict__)
list.append(FlightBean(1, 6, 1, '长安城(157,122)', 30).__dict__)

list.append(FlightBean(1, 1, 2, '长安杂货店(12,11)', 30).__dict__)
list.append(FlightBean(1, 2, 2, '备用棋', 30).__dict__)

str = json.dumps(list).encode('utf-8').decode('unicode_escape')
with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
    f.write(str)
