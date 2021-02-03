from random import randint
from math import sqrt

class Point:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
    #zadanie1
    def move(self, dx, dy):
        self.x = dx
        self.y = dy
    def printCords(self):
        print("X:", self.x, "Y:", self.y)
    #zadanie2
    def pointBetween(self, point):
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y
        if x1 > x2:
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1
        p2 = Point(randint(x1, x2), randint(y1, y2))
        p2.printCords()
    #zadanie3
    def getLineTo(self, point):
        x1 = self.x
        y1 = self.y
        x2 = point.x
        y2 = point.y
        #x1*a + b = y1
        #x2*a + b = y2
        a = y1-y2/(x1-x2)
        b = y1 - (x1 * (y1-y2/(x1-x2)))
        print(a, b)
    #zadanie4
    def distanceTo00(self):
        distance = sqrt(self.x * self.x + self.y * self.y)
        return distance
    def __gt__(self, other):
        return self.distanceTo00() > other.distanceTo00()


class Rectangle:
    def __init__(self, Point=Point(2, 2), dwidth=2, dheight=2):
        self.x = Point.x
        self.y = Point.y
        self.width = dwidth
        self.height = dheight
    def __str__(self):
        return 'x: {}, y: {}, width: {}, height: {}'.format(self.x, self.y,self.width, self.height)
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
    def center(self):
        cx = self.x + self.width/2
        cy = self.y - self.height/2
        return cx, cy
    def contains(self, point):
        if point.x > self.x + self.width or point.x < self.x:
            return "NO"
        elif point.y > self.y or point.y < self.y - self.height:
            return "NO"
        else:
            return "YES"
    def overlap(self, rec):
        if rec.x > self.x or rec.y < self.y:
            return "No"
        elif self.x - rec.x + rec.width < self.width:
            return "No"
        elif rec.y - self.y + rec.height < self.height:
            return "No"
        else:
            return "Yes"


p = Point(0, 0)
p.printCords()
p.move(1, 2)
if p.x == 2 and p.y == 5:
 print('Correct!')
else:
 print('Incorrect!')
p.pointBetween(Point(2,2))
p2 = Point(2, 1)
print("TUTAJ ZADANIE GETLINETO")
p.getLineTo(p2)
if not (Point(0,0) > Point(1,1)) and Point(2,2) > Point(1,1):
    print('Correct!')
else:
    print('Incorrect!')
r = Rectangle()
print(r)
print(r.area())
print(r.perimeter())
print(r.center())
print(r.contains(p2))
pr1 = Point(2, 2)
pr2 = Point(4, 4)
r1 = Rectangle(pr1, 10, 10)
r2 = Rectangle(pr2, 200, 200)
print(r2.overlap(r1))