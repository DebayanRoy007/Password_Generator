#~~~Debayan Roy~~~
import random
import string
import turtle

screen = turtle.Screen()
screen.title("Random Password Generator")
screen.bgcolor("black") 

turtle_pen = turtle.Turtle()
turtle_pen.speed("fastest")  
turtle_pen.hideturtle()

password=''
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
generates = letters + digits + symbols

password_len = int(turtle.textinput("Password Length", "Enter password length:"))

for i in range(password_len):
    password += ''.join(random.choice(generates))

turtle_pen.penup()
turtle_pen.goto(-150, 50)
turtle_pen.color("white")
turtle_pen.write("Your Password:", align="left", font=("Arial", 12, "bold"))
turtle_pen.goto(-150, 30)
turtle_pen.pendown()

turtle_pen.forward(300)
turtle_pen.right(90)
turtle_pen.forward(80)
turtle_pen.right(90)
turtle_pen.forward(300)
turtle_pen.right(90)
turtle_pen.forward(80)
turtle_pen.penup()

turtle_pen.goto(0, 0)
turtle_pen.color("white")
turtle_pen.write(f"{password}", align="center", font=("Arial", 12, "bold"))

turtle.done()

