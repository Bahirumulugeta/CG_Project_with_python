from graphics import *

# input from the user
p = int(input("Enter X coordinate: "))
q = int(input("Enter Y coordinate: "))
r = int(input("Enter radius of the circle: "))

win = GraphWin('Bresenhams circle algorithm', 600, 400)

d = 3 - 2*r  # distance
y = r

x=0 # Initialize   x=0
while x <= y:
    p1 = Point(x + p, y + q)
    p1.draw(win)
    p2=Point (y+p, x+q)
    p2.draw(win)
    p3=Point (-y+p, x+q)
    p3.draw(win)
    p4=Point (-x+p, y+q)
    p4.draw(win)
    p5=Point (-x+p, -y+q)
    p5.draw(win)
    p6=Point (-y+p, -x+q)
    p6.draw(win)
    p7=Point (y+p, -x+q)
    p7.draw(win)
    p8=Point (x+p, -y+q)
    p8.draw(win)
    if d < 0:
        d=d+4*x +6
    else:
        d=d+4*(x-y)+10
        y=y-1
    x=x+1

win.getMouse()
win.close()

