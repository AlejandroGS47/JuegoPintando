"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice

from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


colors = ['black', 'blue', 'purple', 'yellow', 'orange']
directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]

food_color = 'green'  # Color inicial de la comida

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(point):
    """Return True if point is inside boundaries."""
    return -200 < point.x < 190 and -200 < point.y < 190

def move_food():
    """Move food randomly one step and ensure it stays inside the boundaries."""
    global food_color

    move_direction = choice(directions)
    new_food_position = food + move_direction

    if inside(new_food_position):
        food.move(move_direction)

        food_color = choice(colors)  # Cambiar el color de la comida al moverla

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
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, choice(colors))

    square(food.x, food.y, 9, food_color)  # Usar el color actual de la comida
    update()

    move_food()

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
