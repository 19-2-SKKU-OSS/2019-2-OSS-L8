"""Memory, puzzle game of number pairs.
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from time import *
from sys import *
from freegames import path

"Make image dictionary with 3 images"
image_dic = {}
image_dic['car'] = path('car.gif')
image_dic['sea'] = path('sea.gif')
image_dic['jellyfish'] = path('jellyfish.gif')

image = choice(list(image_dic.values()))

tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
revealed_tiles = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global revealed_tiles
        revealed_tiles += 2

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(image)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if(revealed_tiles >= 64):
        up()
        goto(-130, 0)
        write('All tiles were detected', font=('Arial', 25, 'normal'))
        sleep(5)
        exit()


    if mark is not None and hide[mark] is not False:
        x, y = xy(mark)
        up()
        if(tiles[mark] < 10):
            goto(x + 15, y)
        else: goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(image)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
