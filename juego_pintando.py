from turtle import *

from freegames import vector
import math


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def draw_circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    radius = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    circle(radius)

    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Lados del rectángulo
    width = end.x - start.x
    height = end.y - start.y

    for count in range(2):
        forward(width)  # Lado largo
        left(90)
        forward(height)  # Lado corto
        left(90)

    end_fill()



def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calcular el lado del triángulo
    side = end.x - start.x

    for count in range(3):
        forward(side)
        left(120)  # Ángulo para un triángulo equilátero

    end_fill()


def pentagon(start, end):
    """Draw pentagon from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(5):
        forward(end.x - start.x)
        left(72)  # Ángulo para un pentágono regular

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')  # Color nuevo: naranja
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', pentagon), 'p')  # Asignar la tecla 'p' al pentágono
done()

