from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
taps = 0  # Contador de taps

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
    """Convierte las coordenadas (x, y) en un índice de tiles."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte el número de tiles en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Actualiza el marcador y las tiles ocultas según el tap."""
    global taps
    spot = index(x, y)
    mark = state['mark']

    # Incrementa los taps con cada tap válido
    taps += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
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

    # Dibuja los tiles
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # Ajuste para centrar el número
        color('black')
        write(emojis[mark], align="center", font=('Arial', 30, 'normal'))  # Centramos el texto

    if check_win():
        up()
        goto(0, 0)
        color('green')
        write(f"¡Ganaste! con {taps} taps", align="center", font=('Arial', 40, 'bold'))
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
