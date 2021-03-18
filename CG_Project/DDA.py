from graphics import *
import math
win = GraphWin('DDA algorithm with python ', 600, 450)
x1 = 0
x2 = 300
y1 = 0
y2 = 300
dx = x2 - x1
dy = y2 - y1
if(abs(dx) > abs(dy)):
    step = abs(dx)
else:
    step = abs(dy)
xinc = dx/float(step)
yinc = dy/float(step)
for i in range(step):
    if (xinc == 1):
        pt = Point(int(x1), int(y1 + 0.5))
        x1 = x1 + xinc
        y1 = y1 + float(yinc)
    else:
        pt = Point(int(x1 + 0.5), int(y1))
        x1 = x1 + float(xinc)
        y1 = y1 + yinc
    pt.draw(win)
win.getMouse()
win.close()