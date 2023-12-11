import time
from turtle import Screen
from Project_22_class import GeneratePaddle, Ball, ScoreBoard

# TODO 1: CREATE A SCREEN

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")



# TODO 2: CREATE & MOVE PADDLE

paddle = GeneratePaddle()

screen.listen()
screen.onkeypress(fun=paddle.w, key='w')
screen.onkeypress(fun=paddle.s, key='s')
screen.onkeypress(fun=paddle.up, key='Up')
screen.onkeypress(fun=paddle.down, key='Down')


# TODO 3: CREATE THE BALL & MAKE IT MOVE

ball = Ball()
score = ScoreBoard()

game_on = True
while game_on:
    time.sleep(ball.velocity)
    ball.move_ball()
    # TODO 4: DETECT COLLISION WITH WALL & BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_hit()
    # TODO 5: DETECT COLLISION WITH PADDLE
    if ball.distance(paddle.paddle_list[1]) < 50 and ball.xcor() > 320 or ball.distance(paddle.paddle_list[0]) < 50 and ball.xcor() < -320:
        ball.paddle_hit()

# TODO 6: DETECT WHEN PADDLE MISSES
    if ball.xcor() > 380:           # 2nd (right) misses
        ball.reset_ball()
        score.point_1()

    if ball.xcor() < -380:          # 1st (left) misses
        ball.reset_ball()
        score.point_2()

# TODO 7: KEEP SCORES


screen.exitonclick()
