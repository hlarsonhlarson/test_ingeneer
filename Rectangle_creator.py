from math import cos, sin, pi
import numpy as np
from PIL import Image, ImageDraw
import random

MIN_SIZE_BORDER = 120
MAX_SIZE_BORDER = 250
MIN_ANGLE = 0
MAX_ANGLE = 89
WIDTH = 640
HEIGHT = 480

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self):
        left_x = random.randint(0,WIDTH-MAX_SIZE_BORDER)
        while left_x+MAX_SIZE_BORDER > WIDTH:
            left_x = random.randint(0,WIDTH-MAX_SIZE_BORDER)
        left_y = random.randint(0,HEIGHT-MAX_SIZE_BORDER)
        while left_y+MAX_SIZE_BORDER > HEIGHT:
            left_y = random.randint(0,HEIGHT-MAX_SIZE_BORDER)
        left_corner = Point(left_x,left_y)
        right_x = random.randint(left_x+MIN_SIZE_BORDER, left_x+MAX_SIZE_BORDER)
        right_y = random.randint(left_y+MIN_SIZE_BORDER, left_y+MAX_SIZE_BORDER)
        right_corner = Point(right_x,right_y)
        angle = random.randint(MIN_ANGLE,MAX_ANGLE)*pi /180
        print(left_x,left_y,right_x, right_y, angle)
        color = list(np.random.choice(range(256),size=3))
        self.fill_vertixes(left_corner,right_corner,angle,color)

    @staticmethod
    def rotate(vertixes, angle):
        print([(v.x,v.y) for v in vertixes])
        new_vertixes = []
        for elem in vertixes:
            new_x = elem.x * cos(angle) - elem.y * sin(angle)
            new_y = elem.x * sin(angle) + elem.y * cos(angle)
            new_vertixes.append(Point(new_x,new_y))
        x_s = [v.x for v in new_vertixes]
        print(x_s)
        y_s = [v.y for v in new_vertixes]
        if min(x_s) < 0:
            minimum = abs(min(x_s))
            x_s = [v.x+minimum for v in new_vertixes]
        if max(x_s) > WIDTH:
            maximum = abs(max(x_s)) - WIDTH
            x_s = [v.x-maximum for v in new_vertixes]
        print(x_s)
        print(y_s)
        if min(y_s) < 0:
            minimum = abs(min(y_s))
            y_s = [v.y+minimum for v in new_vertixes]
        if max(y_s) > HEIGHT:
            maximum = abs(max(y_s)) - HEIGHT
            y_s = [v.y-maximum for v in new_vertixes]
        print(y_s)
        new_vertixes = [Point(x_s[i],y_s[i]) for i in range(len(x_s))]
        print([(v.x,v.y) for v in new_vertixes])

        return new_vertixes

    def fill_vertixes(self, left_low: Point, right_up: Point, angle: int, color: list) -> None:
        v1 = left_low
        v2 = Point(left_low.x, right_up.y)
        v3 = right_up
        v4 = Point(right_up.x,left_low.y)
        self.vertixes = [v1,v2,v3,v4]
        self.vertixes = self.rotate(self.vertixes,angle)
        self.left_low = self.vertixes[0]
        self.right_up = self.vertixes[2]
        self.color = color
        #print(self.vertixes)


    def draw_rectangle(self):
        color = list(np.random.choice(range(256),size=3))
        #print(color)
        while color[0] == self.color[0] and color[1] == self.color[1] and color[2] == self.color[2]:
            color = list(np.random.choice(range(256),size=3))
        image = Image.new("RGB", (WIDTH, HEIGHT), color=tuple(color))
        draw = ImageDraw.Draw(image)
        v1,v2,v3,v4 = self.vertixes
        print([(v.x,v.y) for v in self.vertixes])
        draw.polygon([(v.x,v.y) for v in self.vertixes],fill=tuple(self.color))
        return image, tuple([v2.x,v2.y,v3.x-v1.x,v3.y-v1.y]),tuple([(v.x,v.y) for v in self.vertixes]) 

if __name__ == '__main__':
    rect = Rectangle()
    image, outlining_rect,coords = rect.draw_rectangle()
    print(coords)
    #print([(v.x,v.y) for v in coords])
    image.show()
