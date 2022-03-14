import turtle
import time
import random
from random import randint
from turtle import Turtle, Screen

delay = 0

score = 0
high_score = 0

#the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("red")
# snake.goto(0, 0) - might not need this as the snake goes straight to the center point
snake.penup() #this will prevent the path the snake takes from being drawn
#snake.speed(0)
#snake.direction = "stop"

#main screen
screen = turtle.Screen()
screen.title('The Ultimate Snake Game')
screen.bgcolor('green') #screen colour - green
#screen.tracer(0, 0) #This function will prevent screen updates. Therefore, needs to be set to 0. The only thing that needs to update is the score everytime the snake eats.
screen.setup(width=400, height=400) #screen size

#movement
speed = 1

def movement():
  snake.forward(speed)
  screen.ontimer(movement, 10)

screen.onkey(lambda: snake.setheading(90), "Up")
screen.onkey(lambda: snake.setheading(180), "Left")
screen.onkey(lambda: snake.setheading(0), "Right")
screen.onkey(lambda: snake.setheading(270), "Down")

screen.listen()

movement()

main.loop() #turtles continous movement - whilst there is no movement the snake will forward inifintely :)



  

#press space bar to initiate game (could be displayed as a button)



#score

  #increases with eating the food
  #will chnage if surpasses the score of the person in first place on the leader 

#main game

#leaderboard

  #displayed at the top
  #displayed at the end



#border that if the snake touches the game will automatically end

#snake (colour, increases everytime it eats)
#movements
#start the game
#Display of the highscore
#leaderboard (optional)

#the food
#food = turtle.Turtle()
#food.color("black")
#food.shape("circle")
#food.penup()
#food.goto(randint(-100,0),randint(0,100)) 


#turtle.done()