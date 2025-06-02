import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("lightblue")
drawing_board.title("Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.right(10)

def rotate_angle_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def penup():
    turtle_instance.penup()

def pendown():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=penup, key="u")
drawing_board.onkey(fun=pendown, key="d")

turtle.mainloop()