import turtle
#Отобразил курсор
# turtle.showturtle()
#
# #Направление курсора
# turtle.right(30)
# turtle.left(60)
#
# #Движение черепашки
# turtle.forward(155)
# turtle.backward(250)
#
#
# #Жесткая установка угла
# turtle.setheading(0)
# turtle.forward(100)
# turtle.setheading(90)
#
# turtle.forward(100)
# turtle.setheading(180)
#
# turtle.forward(100)
# turtle.setheading(270)
#
# turtle.forward(100)
#
# turtle.setheading(360)
# #Можем получить актуальный угол направления черепашки
# print(turtle.heading())
#
# #Изменение формы
#
# # turtle.shape('turtle')
# # turtle.Screen().addshape('shape.jpg')  # регистрируем изображение
# # turtle.shape('shape.jpg')
# turtle.forward(100)
#
# turtle.clear()
#
# def rectangle(width, height):
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#
# rectangle(100, 150)
#
#
# def triangle(side):
#     turtle.forward(side)
#     turtle.left(120)
#     turtle.forward(side)
#     turtle.left(120)
#     turtle.forward(side)
#
#
# # triangle(150)
#
#
# def square(side):
#   turtle.left(22)
#   turtle.forward(side)
#   turtle.left(90)
#   turtle.forward(side)
#   turtle.left(90)
#   turtle.forward(side)
#   turtle.left(90)
#   turtle.forward(side)
#
# # for i in range(3):
# #   square(150)
# #   turtle.left(90)
#
#
# import turtle
# import random
#
# import turtle
# import random
#
#
# def square(side):
#     turtle.left(22)
#     turtle.forward(side)
#     turtle.left(90)
#     turtle.forward(side)
#     turtle.left(90)
#     turtle.forward(side)
#     turtle.left(90)
#     turtle.forward(side)
#
#
# turtle.Screen().bgcolor("pink")
# turtle.speed(100)
# for i in range(100):
#     turtle.pencolor(random.choice(['green', 'red', 'blue', 'yellow']))
#     square(150)
#     turtle.left(90)
#
#
# turtle.done()
#
# import turtle
#
#
# def move_up():  # функция обратного вызова
#     x, y = turtle.pos()
#     turtle.setposition(x, y + 5)
#
#
# def move_down():  # функция обратного вызова
#     x, y = turtle.pos()
#     turtle.setposition(x, y - 5)
#
#
#
# import turtle
#
# pen = turtle.Turtle()
# pen.color("red")
# pen.pensize(2)
#
# def draw_triangle():
#     for _ in range(3):
#         pen.forward(100)
#         pen.left(120)




#
# def move_left():  # функция обратного вызова
#     x, y = turtle.pos()
#     turtle.setposition(x - 5, y)
#
#
# def move_right():  # функция обратного вызова
#     x, y = turtle.pos()
#     turtle.setposition(x + 5, y)
#
#
# turtle.showturtle()  # отображаем черепашку
# turtle.pensize(3)  # устанавливаем размер пера
# turtle.shape('turtle')
# turtle.Screen().listen()  # устанавливаем фокус на экран черепашки
#
# turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
# turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
# turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
# turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо


screen = turtle.Screen()
t = turtle.Turtle()

# Шаг 1: Рисуем круг
t.penup()
t.goto(0, -100)  # Перемещаем черепаху к центру экрана
t.pendown()
t.circle(100)  # Рисуем круг радиусом 100

# Шаг 2: Рисуем квадрат
t.penup()
t.goto(0, 0)  # Перемещаем черепаху в центр круга
t.pendown()
t.forward(100)  # Рисуем сторону квадрата
t.left(90)  # Поворачиваем налево на 90 градусов
t.forward(100)  # Рисуем вторую сторону
t.left(90)
t.forward(100)  # Рисуем третью сторону
t.left(90)
t.forward(100)  # Рисуем четвертую сторону
t.left(90)

# Завершаем программу
turtle.done()
