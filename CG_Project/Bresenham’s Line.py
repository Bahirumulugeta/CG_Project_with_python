from graphics import *
import math
win = GraphWin('Bresenham line Algorithm ', 600, 400)


def sign(inp):  # to check direction of line
    if inp > 0:
        ret = 1
    elif inp < 0:
        ret = -1
    else:
        ret = 0
    return ret


x1 = 100  # starting point on x
y1 = 50  # starting point on y
x2 = 100  # end point on x
y2 = 120  # end point in y

x = x1
y = y1
dx = abs(x2 - x)  # change in x
dy = abs(y2 - y)  # change in y
s1 = sign(x2 - x1)
s2 = sign(y2 - y1)

if dy > dx:  # sweeping action needed
    dx, dy = dy, dx
    change = True
else:
    change = False

p = 2 * dy - dx

for i in range(dx):
    pt = Point(x, y)
    pt.draw(win)
    if (p < 0):
        if change:
            y = y + s2
        else:
            x = x + s1
        p = p + 2 * dy
    else:
        if change:
            x = x + s1
        else:
            y = y + s2
        p = p - 2 * dx
win.getMouse()
win.close()
