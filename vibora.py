from turtle import * 
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    
        


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    "Variable escoge la direccion del movimiento de la comida"
    r=randrange(4) 
    "Booleano para revisar que la comida se haya movido un paso" 
    check=False 
    "El ciclo correra hasta que la comida se haya podido mover dentro de los limites del area de juego"
    while check==False: 
        if r==0:
            "Los ifs compruban que la comida se pueda mover sin salirse del rango"
            if food.x <=140:
                food.x=food.x+10
                "Si se mueve la comida se completa el ciclo"
                check=True
            else:
                r=randrange(4)
        if r==1:
            if food.x >=-140:
                food.x=food.x-10
                check=True
            else:
                r=randrange(4)
        if r==2:
            if food.y <=140:
                food.y=food.y+10
                check=True
            else:
                r=randrange(4)
        if r==3:
            if food.y >=-140:
                food.y=food.y-10
                check=True
            else:
                r=randrange(4)
        

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
