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

from freegames import path

car = path('car.gif')

emojis = ['🍎', '🍌', '🍇', '🍉', '🍓', '🍒', '🍍', '🥝', '🍋', '🍑', '🍐', '🍈', '🍏', '🥭', '🍊', '👌', 
          '❤️', '🥥', '🍆', '🥑', '🌽', '🥕', '🥒', '🥬', '🥦', '🍄', '🌶', '🥔', '🍠', '🍯', '🍞', '🧀'] * 2

state = {'mark': None}
hide = [True] * 64

def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
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
    """Convierte las coordenadas (x, y) a índice de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte el índice de fichas a coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Actualiza la marca y oculta las fichas según el toque."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or emojis[mark] != emojis[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def check_win():
    """Verifica si todos los cuadros están destapados."""
    return not any(hide)

def draw():
    """Dibuja la imagen y las fichas."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(emojis[mark], font=('Arial', 30, 'normal'))

    if check_win():
        up()
        goto(0, 0)
        color('green')
        write("¡Ganaste!", align="center", font=('Arial', 40, 'bold'))
    else:
        update()
        ontimer(draw, 100)

shuffle(emojis)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

