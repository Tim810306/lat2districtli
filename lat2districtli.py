# -*- coding: UTF-8 -*-
def search(x, y):  #尋找鄉鎮
    global shapes, villnames
    return next((villnames[vill_id]  #如果鄉鎮區域包含傳入的經緯度就傳回townnames[town_id]
                 for vill_id in shapes  #逐一尋找各鄉鎮
                 if shapes[vill_id].contains(Point(x, y))), None)

import fiona
from shapely.geometry import shape, Point
import os

# lng = float(input('輸入經度：'))
# lat = float(input('輸入緯度：'))
module_dir = os.path.dirname(__file__)  #取得目前目錄
collection = fiona.open(os.path.join(module_dir, 'VILLAGE_MOI_1101214.shp'),  encoding='utf-8')
shapes = {}
villnames = {}

for f in collection:
    vill_id = f['properties']['VILLCODE']  #鄉鎮代碼
    shapes[vill_id] = shape(f['geometry'])  #鄉鎮界限經緯度
   
    # print(str(f['properties']['VILLNAME']))
    villnames[vill_id] = f['properties']['COUNTYNAME'] + ',' + f['properties']['TOWNNAME'] + ',' + f['properties']['VILLNAME'] #search函式傳回值

print(search(float(121.567331), float(25.0415812)))
