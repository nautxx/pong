from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# initialize screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Poooooong")
screen.tracer(0) #turns off animation so while loop is needed to manually turn on animation

# initialize objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# have screen listen for keystrokes
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a") # buttons 'q' and 'w' can't be held down
screen.onkey(l_paddle.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.move_faster()
        ball.bounce_x()

    # detect when ball goes out of bounds to the right
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset()
    
    # detect when ball goes out of bounds to the left
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset()

screen.exitonclick()