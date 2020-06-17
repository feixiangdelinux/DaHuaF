from DisposeUtil import read_ispose
import json
str = read_ispose('E:\BtcProfile.txt')
print('250:  fdafads')
print(str)
myClassReBuild = json.loads(str)
print (myClassReBuild)