#The inital part of the game

import turtle
import time
import random 

score = 0
high_score = 0
delay = 0

#main screen
screen = turtle.Screen()
screen.title('The Ultimate Snake Game Bro')
screen.bgcolor('green') #screen colour - green
screen.tracer(0) #This function will prevent screen updates. Therefore, needs to be set to 0. The only thing that needs to update is the score everytime the snake eats.

#screen size

screen.setup(width=750, height=600)
#screen.screensize(canvwidth=750, canvheight=500) - this does not work because you need to scroll to get to different areas of the screen which will not be easy when playing the game.


  
  #press space bar to initiate game (could be displayed as a button)


#keyboard movements

  # w = 'up'
  # a = 'left'
  # s = 'down'
  # d = 'right'

#the food/ colliding with the food
  
  #increases score
  #increases the size of the snake

#score

  #increases with eating the food
  #will chnage if surpasses the score of the person in first place on the leader board

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
