import time
from turtle import Screen, Turtle
from gamepad import Gamepad
from ball import Ball
from scoreboard import Scoreboard
pong = Turtle("square")
screen = Screen()
ball = Ball()
score = Scoreboard()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
pong.penup()
pong.hideturtle()
pong.goto(x=0, y=-280)
pong.color("white")
pong.seth(90)
pong.pensize(20)
pong.pendown()
for i in range(13):
    pong.forward(20)
    pong.penup()
    pong.forward(30)
    pong.pendown()
pong.penup()


r_gamepad = Gamepad((350, 0))
l_gamepad = Gamepad((-350, 0))

screen.listen()
screen.onkey(r_gamepad.move_up, "Up")
screen.onkey(r_gamepad.move_back, "Down")
screen.onkey(l_gamepad.move_up, "w")
screen.onkey(l_gamepad.move_back, "s")
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect ball hits wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detects when ball hits gamepad
    if (ball.distance(r_gamepad) < 50 and ball.xcor() > 320) or (ball.distance(l_gamepad) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detects when right side misses ball
    if ball.xcor() > 380:
        ball.out_of_bounds()
        score.l_score += 1
        score.point()

    if ball.xcor() < -380:
        ball.out_of_bounds()
        score.r_score += 1
        score.point()

screen.exitonclick()
