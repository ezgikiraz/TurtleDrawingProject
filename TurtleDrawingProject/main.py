import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("python turtle")


'''
turtle_instance2 = turtle.Turtle()
turtle_instance2.left(90)
turtle_instance2.forward(100)
'''

#square
'''
turtle_instance3 = turtle.Turtle()
for i in range (4):
    turtle_instance3.forward(100)
    turtle_instance3.left(90)


#star
turtle_instance4 = turtle.Turtle()

for i in range (5):
    turtle_instance4.right(144)
    turtle_instance4.forward(100)



turtle_instance4 = turtle.Turtle()
num_side = 7
angle = 360.0 / num_side
side_length = 100

for i in range (num_side):
    turtle_instance4.right(angle)
    turtle_instance4.forward(side_length)

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5
shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
shrinkingSquare(10)

turtle_instance = turtle.Turtle()
turtle_instance.color("red")
turtle.speed(0)
turtle_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(15):
    turtle_instance.color(turtle_colors[i%6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)
turtle.done()

'''