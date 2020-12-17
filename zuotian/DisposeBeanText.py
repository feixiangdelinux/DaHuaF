import json

from zuotian.DisposeBean import FlightBean

file_path = 'E://Dahua/'
list = []
list.append(FlightBean(1, 1, 1, '长安城(199,72)', 30).__dict__)
list.append(FlightBean(1, 1, 2, '长安城(138,44)', 30).__dict__)
list.append(FlightBean(1, 1, 3, '长安城(126,13)', 30).__dict__)
list.append(FlightBean(1, 1, 4, '长安城(16,135)', 30).__dict__)
list.append(FlightBean(1, 1, 5, '长安城(44,124)', 30).__dict__)
list.append(FlightBean(1, 1, 6, '长安城(80,138)', 30).__dict__)

list.append(FlightBean(1, 2, 1, '备用棋', 30).__dict__)

str = json.dumps(list).encode('utf-8').decode('unicode_escape')
with open(file_path + 'FlightChessProfile.txt', 'w', encoding='utf-8') as f:
    f.write(str)
