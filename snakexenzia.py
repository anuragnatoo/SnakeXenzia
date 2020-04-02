# -*- coding: utf-8 -*-
"""
Created on Thu Apr 2  2020

@author: Anurag Natoo
"""
import os
import turtle
import time
import random

delay=0.15
# Screen setup
# My screen size- 1366 x 768
wind=turtle.Screen()
wind.title("Snake Game")
wind.bgcolor("white")
wind.setup(width=666,height=768)
wind.tracer(0) #Turns animation off
# tracer 0 also turns off the screen updates

# Snake Head
head=turtle.Turtle()
head.speed(0)# Animation speed is 0
head.shape("circle")
head.color("black")
head.penup() #no drawing when moving.
head.goto(0,0) #When head starts it will be @ centre of screen
head.direction="stop"

# Snake Food
food=turtle.Turtle()
food.speed(0)# Animation speed is 0
food.shape("square")
food.color("blue")
food.penup() #no drawing when moving.
food.goto(0,0) #When head starts it will be @ centre of screen

# Scoreboard
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write("Score : 0  High Score : 0",align="center",font=("Verdana",24,"normal"))
# Snake Body
segments=[]
score=-10
high_score=-10
# Directions
def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_left():
    if head.direction != "right":
        head.direction="left"
def go_right():
    if head.direction != "left":
        head.direction="right"

# Keyboard Bindings
wind.listen()
wind.onkeypress(go_up,"Up")
wind.onkeypress(go_down,"Down")
wind.onkeypress(go_left,"Left")
wind.onkeypress(go_right,"Right")
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
'''
Main Game Loop
'''
while True:
    wind.update()
    #Collison handling
    if head.xcor()>300 or head.xcor()<-300 or head.ycor()<-300 or head.ycor()>300:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        # Hide the segments or remove the segments
        for i in segments:
            i.goto(10000,10000)
        segments.clear() 
        # Delay reset
        delay=0.15
        # Reset Score
        score=0
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("Verdana",24,"normal"))
   

    if head.distance(food) < 20:
        # Move the food to a random positon
        xnew = random.randint(-300,300)
        ynew = random.randint(-300,300)
        food.goto(xnew,ynew)
        # Add a new segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("circle")
        new_segment.color("grey")
        segments.append(new_segment)
        # Increase the speed
        delay=delay-0.01
        # Increment Score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("Verdana",24,"normal"))
    # Move the end segments in reverse order                
    for index in range(len(segments)-1,0,-1):
        xprev=segments[index-1].xcor()
        yprev=segments[index-1].ycor()
        segments[index].goto(xprev,yprev)
    # Move segment 0 to where the head is
    if  len(segments)>0:
        xhead=head.xcor()
        yhead=head.ycor()
        segments[0].goto(xhead,yhead)
    move()
    # Check for body collisions
    for a in segments:
        if a.distance(head)<20:
            time.sleep(0)
            head.goto(0,0)
            head.direction="stop"
            for p in segments:
                p.goto(10000,10000)
            segments.clear()
            # Reset Score
            score=0
            delay=0.15
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("Verdana",24,"normal"))
    time.sleep(delay)
    
wind.mainloop()# This keeps the window running