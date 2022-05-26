from plot3DColorSpace import *
import math

# 緑系統のプロット
red   =[120,154,  0,173,  0]
green =[195,205,255,255,128]
blue  =[13, 50,  0, 47,  0]
name = ["黄緑っぽい", "yellowgreen", "lime", "greenyellow", "green"]

print("黄緑っぽいからの距離")

for i in range(1,len(red)):
    length = math.sqrt((red[0] - red[i])**2+(green[0] - green[i])**2+(blue[0] - blue[i])**2)
    print(" {1:>11s}:{0:5.1f}".format(length.real, name[i]))

greenPlot = plot3DColorSpace(red, green, blue, name)
greenPlot.step = 16
greenPlot.plot("greenColors.html")

# 1辺が6の立方体の中にある白のプロット
red, green, blue, name = [], [], [], []

width = 5
for r in range(width + 1):
    for g in range(width + 1):
        for b in range(width + 1):
            r_ap, g_ap, b_ap = int(255 - r), int(255 - g), int(255 - b)
            red.append(r_ap)
            green.append(g_ap)
            blue.append(b_ap)

squarePlot = plot3DColorSpace(red, green, blue)
squarePlot.step = 1
squarePlot.plot("squreWhite.html")

# 真っ白からの距離が一定よりも近い距離にある白
red, green, blue, name = [], [], [], []

radius = 6.48
counter = 0

for r in range( math.ceil(radius)+1):
    for g in range(math.ceil(radius)+1):
        for b in range(math.ceil(radius)+1):
            r_ap, g_ap, b_ap = int(255 - r), int(255 - g), int(255 - b)
            distance = math.sqrt((255-r_ap)**2+(255-g_ap)**2+(255-b_ap)**2)
            if(distance<=radius):
                red.append(r_ap)
                green.append(g_ap)
                blue.append(b_ap)
                counter+=1
           
print("半径：{0}, 点の個数：{1}".format(radius, counter))

whiteBallPlot = plot3DColorSpace(red, green, blue)
whiteBallPlot.step = 1
whiteBallPlot.plot("ballWhite.html")
