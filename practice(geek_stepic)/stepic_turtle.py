import turtle
#Отобразил курсор
turtle.showturtle()

#Направление курсора
turtle.right(30)
turtle.left(60)

#Движение черепашки
turtle.forward(155)
turtle.backward(250)


#Жесткая установка угла
turtle.setheading(0)
turtle.forward(100)
turtle.setheading(90)

turtle.forward(100)
turtle.setheading(180)

turtle.forward(100)
turtle.setheading(270)

turtle.forward(100)

turtle.setheading(360)
#Можем получить актуальный угол направления черепашки
print(turtle.heading())

#Изменение формы

# turtle.shape('turtle')
# turtle.Screen().addshape('shape.jpg')  # регистрируем изображение
# turtle.shape('shape.jpg')
turtle.forward(100)

turtle.clear()

def rectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

rectangle(100, 150)


def triangle(side):
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)


# triangle(150)


def square(side):
  turtle.left(22)
  turtle.forward(side)
  turtle.left(90)
  turtle.forward(side)
  turtle.left(90)
  turtle.forward(side)
  turtle.left(90)
  turtle.forward(side)

# for i in range(3):
#   square(150)
#   turtle.left(90)


import turtle
import random

import turtle
import random


def square(side):
    turtle.left(22)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)


turtle.Screen().bgcolor("pink")
turtle.speed(100)
for i in range(100):
    turtle.pencolor(random.choice(['green', 'red', 'blue', 'yellow']))
    square(150)
    turtle.left(90)


turtle.done()

