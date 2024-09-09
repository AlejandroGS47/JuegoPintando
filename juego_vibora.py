from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Definir las posibles direcciones en las que la comida puede moverse
directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(point):
    """Return True if point is inside boundaries."""
    return -200 < point.x < 190 and -200 < point.y < 190


def move_food():
    """Move food randomly one step and ensure it stays inside the boundaries."""
    move_direction = choice(directions)
    new_food_position = food + move_direction

    # Verificar que la comida no se salga de los límites
    if inside(new_food_position):
        food.move(move_direction)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        # En lugar de mover la comida a una posición aleatoria, movemos un paso
        move_food()
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

