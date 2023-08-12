#pong made by me
#part1 : getting started
from operator import truediv
from tkinter.tix import Balloon

import turtle
import winsound

wn= turtle.Screen()
wn.title("pong by me")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
Ball = turtle.Turtle()
Ball.speed(5)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx= 0.2
Ball.dy= -0.2

#pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0   player B: 0", align= "center", font= ("times new roman", 24, "normal"))

#score
score_A= 0
score_B= 0


#function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#function
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    #move the ball
    Ball.setx(Ball.xcor() +Ball.dx)
    Ball.sety(Ball.ycor() +Ball.dy)

    #border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)

    if Ball.xcor()> 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_A +=1
        pen.clear()
        pen.write("player A: {}   player B: {}".format(score_A, score_B), align= "center", font= ("times new roman", 24, "normal"))
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)

    if Ball.xcor()< -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("player A: {}   player B: {}".format(score_A, score_B), align= "center", font= ("times new roman", 24, "normal"))
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)

    #paddle and ball collision
    if Ball.xcor() > 340 and Ball.xcor()< 350 and (Ball.ycor() < paddle_b.ycor() + 50 and Ball.ycor() > paddle_b.ycor() -50):
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)

    if Ball.xcor() < -340 and Ball.xcor()> -350 and (Ball.ycor() < paddle_a.ycor() + 50 and Ball.ycor() > paddle_a.ycor() -50):
        Ball.setx(-340)
        Ball.dx *= -1    
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)
