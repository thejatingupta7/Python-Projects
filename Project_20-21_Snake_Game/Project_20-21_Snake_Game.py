import turtle
from turtle import Turtle, Screen
import time
from Project_20_21_Snake_class import Snake, Food, ScoreBoard

# TODO 1: Create a Snake body

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=650)     # x=350, y=325
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()

# TODO 3: Control the Snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



# TODO 2: Move the Snake
screen.tracer(0)
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO 4: Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_tim()
        score.increase_score()          # TODO 5: Create a scoreboard
        score.update_score()


    # TODO 6: Detect collision with wall
    if snake.snake_head.xcor() > 340 or snake.snake_head.xcor() < -340 or snake.snake_head.ycor() > 315 or snake.snake_head.ycor() < -315:
        score.reset()
        snake.reset_tim_list()

    # TODO 7: Detect collision with tail
    for segment in snake.tim_list:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset_tim_list()


screen.exitonclick()





