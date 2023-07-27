from turtle import Screen,Turtle
from Paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time


screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
ball_speed = 0.1



ball=Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreBoard = ScoreBoard()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # bouncing of ball and paddle collison

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50) and (ball.xcor()>320 or ball.xcor()<-320)):
        print("Collision detected")
        ball.bounce_x()
        ball_speed = ball_speed-0.01



    # wall collsion

    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreBoard.l_point()
        ball_speed=0.1


    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreBoard.r_point()
        ball_speed=0.1
        

screen.exitonclick()

