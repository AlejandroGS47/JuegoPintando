from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Cambia el tamaño de la cuadrícula a 8x8 (64 tiles, es decir, 32 pares)
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0  # Contador de taps

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

def draw():
    """Dibuja la imagen y los tiles."""
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
        goto(x + 10, y + 5)  # Centrar el número de un solo dígito
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Verifica si todos los tiles han sido revelados
    if all(not hidden for hidden in hide):
        up()
        goto(0, 0)
        color('black')
        write(f"¡Juego Terminado! Total de taps: {taps}", align="center", font=('Arial', 20, 'normal'))
    else:
        update()
        ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

