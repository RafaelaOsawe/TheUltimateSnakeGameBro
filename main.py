#you need to press the screen before you start playing the game
#This is a link to the doc for me to keep track of everything, if anyone wants to see it https://docs.google.com/document/d/12JGvGMXNMb6fx5LM-fM_Zi4aMdBu-Y8woQIYKG1u0SE/edit?usp=sharing
import turtle
import time
import random
import sys
from turtle import *

delay = 0.1

#score variables
high_score = 0
score = 0

#width and height
width = 650
height = 400

minX, maxX = -width/2, width/2
minY, maxY = -width/2, width/2

#window screen
screen = turtle.Screen()
screen.title('The Ultimate Snake Game')
screen.bgcolor('green')
screen.setup(width, height)
screen.tracer(0) 

#the snake head
snake = turtle.Turtle()
snake.shape('square')
snake.color('red')
snake.penup()
snake.goto(0, 0)
snake.direction = 'Stop'

#the food
food = turtle.Turtle()
colours = random.choice(['pink', 'blue', 'black', 'yellow', 'purple', 'white'])
food.color(colours)
food.shape("circle")
food.speed(0)
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 100)

#scores at the top of the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 170)
pen.write('Score: 0    Highscore: 0', align='center', font=('Courier', 15, 'normal'))

#keybinds functions for movement
def go_up():
  snake.setheading(90)
  snake.forward(20)

def go_down():
  snake.setheading(270)
  snake.forward(20)

def go_left():
  snake.setheading(180)
  snake.forward(20)

def go_right():
  snake.setheading(0)
  snake.forward(20)
  
turtle.listen()

turtle.onkey(go_up, 'w') #press your 'w' key to move
turtle.onkey(go_down, 's') #press your 's' key to move
turtle.onkey(go_left, 'a') #press your 'a' key to move
turtle.onkey(go_right, 'd') #press your 'd' key to move

#collision detection
if snake.distance(food) < 20:
  x = random.randint (-250, 250)
  y = random.randint (-250, 250)
  food.goto(x, y)

#main gameplay
while True:
  screen.update()

#border restrictions
def border_restrictions():
  if snake.ycor() >= maxY or snake.ycor() <= minY or snake.xcor() >= maxX or snake.xcor <= minX:
    snake.bye()
    sys.exit(0)

border_restrictions()

turtle.mainloop() #needs to stay at the end

#border collision

#body collision

#score updates





