from cmath import cos, sin
import random

MIN_SIZE_BORDER = 120
MAX_SIZE_BORDER = 250
MIN_ANGLE = 0
MAX_ANGLE = 89
WIDTH = 640
HEIGHT = 480

#size 640*480
#storona ot 150 do 250 px
#ugol 0 do 89
#random color

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Rectangle():
    @staticmethod
    def rotate(vertixes, angle):
        new_vertixes = []
        for elem in vertixes:
            new_x = elem.x * cos(angle) - elem.y * sin(angle)
            new_y = elem.x * sin(angle) + elem.y * cos(angle)
            new_vertixes.append(Point(new_x,new_y))
        return new_vertixes

    def __init__(self, left_low: Point, right_up: Point, angle) -> None:
        v1 = left_low
        v2 = Point(left_low.x, right_up.y)
        v3 = right_up
        v4 = Point(right_up.x,left_low.y)
        self.vertixes = [v1,v2,v3,v4]
        self.vertixes = self.rotate(self.vertixes,angle)
        self.left_low = self.vertixes[0]
        self.right_up = self.vertixes[2]


class CreateRandomRectangle():
    def create_random_rectangle(self):
        left_x = random.randint(0,WIDTH-MIN_SIZE_BORDER)
        left_y = random.randint(0,HEIGHT-MIN_SIZE_BORDER)
        left_corner = Point(left_x,left_y)
        right_x = random.randint(left_x, min(WIDTH,left_x+MAX_SIZE_BORDER))
        right_y = random.randint(left_y, min(HEIGHT,left_x+MAX_SIZE_BORDER))
        right_corner = Point(right_x,right_y)
        angle = random.randint(MIN_ANGLE,MAX_ANGLE)
        rect = Rectangle(left_corner,right_corner,angle)
        return rect

    def draw_rectangle(self):
        pass
