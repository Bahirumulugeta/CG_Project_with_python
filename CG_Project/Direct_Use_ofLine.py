from graphics import *
import math

win = GraphWin('Direct use of line Algorithm ', 600, 400)

# Initialization of variables
x1 = 10
y1 = 20
x2 = 100
y2 = 20

dx = x2 - x1
dy = y2 - y1
m = dy/dx
b = y1 - (m * x1)
if dx < 0:
    x = x2
    y = y2
    xf = x1
else:
    x = x1
    y = y1
    xf = x2
while x < xf:
    ptt = Point(x, y)
    ptt.draw(win)
    x += 1
    y = (m * x) + b
win.getMouse()
win.close()
