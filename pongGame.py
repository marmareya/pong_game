# Classic Pong Game
# Source: https://www.youtube.com/watch?v=LH8WgrUWG_I&list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
# Modified by: Eng. Mariam Ahmed


# Import module(s) used
import turtle
import os


# Initializing window       #General Coordinates: Center = (0,0) Top Right = (300, 400) Bottom Left = (-300, -400)
wn = turtle.Screen()
# title, bgcolor, setup, tracer
wn.title("Pong by @Marmareya")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


# Initializing variables for scores
score_a = 0
score_b = 0

## Paddle A ##       # turtle: Module name   Turtle: Class name
paddle_a = turtle.Turtle()
# Speed of animation
paddle_a.speed(0)
# Define shape
paddle_a.shape("square")
# Set shape size
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# Define color
paddle_a.color("white")
# Raise pen to stop tracing
paddle_a.penup()
# Take Paddle A to coordinate defined
paddle_a.goto(-350,0)

## Paddle B ##
paddle_b = turtle.Turtle()
# Speed of animation
paddle_b.speed(0)
# Define shape
paddle_b.shape("square")
# Set shape size
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# Define color
paddle_b.color("white")
# Raise pen to stop tracing
paddle_b.penup()
# Take Paddle B to coordinate defined
paddle_b.goto(350,0)


## Ball ##
ball = turtle.Turtle()
# Speed of animation
ball.speed(0)
# Define shape. Default size is 20*20 pixels
ball.shape("circle")
# Define color
ball.color("white")
# Raise pen to stop tracing
ball.penup()
# Take Paddle A to coordinate defined
ball.goto(0,0)
# Change in x-direction
ball.dx = 0.07
# Change in y-direction
ball.dy = 0.07


## Pen ##
pen = turtle.Turtle()
# Speed of animation
pen.speed(0)
# Define color
pen.color("white")
# Raise pen to stop pen from drawing lines when moving it around window
pen.penup()
# Hide pen
pen.hideturtle()
# Print initial score at top of game window
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

## Functions ##
# Function to move Paddle A UP on the game window
def paddle_a_up():
    # Assign value of y-coordinate of object Paddle A to variable 'y'
    y = paddle_a.ycor()
    #IF: Paddle still didn't reached border?
    if y < 250:
        # Move paddle up
        y += 20
        # Set new value for y-coordinate to Paddle A
        paddle_a.sety(y)

# Function to move Paddle A DOWN on the game window
def paddle_a_down():
    # Assign value of y-coordinate of object Paddle A to variable 'y'
    y = paddle_a.ycor()
    #IF: Paddle still didn't reached border?
    if y > -240:
        # Move paddle down
        y -= 20
        # Set new value for y-coordinate to Paddle A
        paddle_a.sety(y)

# Function to move Paddle B UP on the game window
def paddle_b_up():
    # Assign value of y-coordinate of object Paddle B to variable 'y'
    y = paddle_b.ycor()
    # IF: Paddle still didn't reached border?
    if y < 250:
        # Move paddle up
        y += 20
        # Set new value for y-coordinate to Paddle B
        paddle_b.sety(y)

# Function to move Paddle B DOWN on the game window
def paddle_b_down():
    # Assign value of y-coordinate of object Paddle B to variable 'y'
    y = paddle_b.ycor()
    # IF: Paddle still didn't reached border?
    if y > -240:
        # Move paddle down
        y -= 20
        # Set new value for y-coordinate to Paddle B
        paddle_b.sety(y)

# Function to update score
def update_score():
    # Clear previous pen writing
    pen.clear()
    # Print updated score
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
    # IF: Check if player A got 5 points to announce win and exit program
    if score_a >= 5:
        # Print winner message
        pen.goto(0, 0)
        pen.write("Player A has won!", align='center', font=('Courier', 24, 'normal'))
        # End program upon user click
        wn.exitonclick()  # IF: Check if player B got 5 points to announce win and exit program
    if score_b >= 5:
        # Print winner message
        pen.goto(0, 0)
        pen.write("Player B has won!", align='center', font=('Courier', 24, 'normal'))
        # End program upon user click
        wn.exitonclick()

        # End program upon user click



## Keyboard Binding ##
# Enabling keyboard listening
wn.listen()
# Setting functions to be executed when certain keys pressed (i.e. "w", "s", "Up", "Down")
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


## Main Game Loop ##
while True:
    # Update window
    wn.update()
    # Update ball position in both x and y directions
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## Border Checking ##
    # IF: Upper border
    if ball.ycor() > 290:
        ball.sety(290)
        # Reverse direction of ball motion
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    # IF: Lower border
    if ball.ycor() < -290:
        ball.sety(-290)
        # Reverse direction of ball motion
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    # IF: Right border
    if ball.xcor() > 390:
        # Place ball back in center
        ball.goto(0, 0)
        # Reverse direction of ball motion
        ball.dx *= -1
        # Add point to Player A's score
        score_a += 1
        # Call update_score() function
        update_score()

    # IF: Left border
    if ball.xcor() < -390:
        # Place ball back in center
        ball.goto(0, 0)
        # Reverse direction of ball motion
        ball.dx *= -1
        # Add point to Player B's score
        score_b += 1
        # Call update_score() function
        update_score()

    ## Paddle + Ball Hits ##
    # IF: Paddle A hits ball
    if (ball.xcor() < -330) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        # Reverse x-direction of ball
        ball.setx(-330)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    # IF : Paddle B hits ball
    if (ball.xcor() > 330) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        # Reverse x-direction of ball
        ball.setx(330)
        ball.dx *= -1
        os.system("aplay bounce.wav&")