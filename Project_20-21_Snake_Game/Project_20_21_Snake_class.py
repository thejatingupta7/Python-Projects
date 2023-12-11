from turtle import Turtle
import random
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



class Snake:

    def __init__(self):
        self.tim_list = []
        self.create_snake()
        self.snake_head = self.tim_list[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_to_tim(i)

    def add_to_tim(self, i):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.pu()
        tim.goto(i)
        self.tim_list.append(tim)

    def reset_tim_list(self):
        for i in self.tim_list:
            i.goto(1000, 1000)
        self.tim_list.clear()
        self.create_snake()
        self.snake_head = self.tim_list[0]

    def extend_tim(self):
        self.add_to_tim(self.tim_list[-1].position())

    def move(self):
        for segment in range(len(self.tim_list) - 1, 0, -1):
            new_x = self.tim_list[segment - 1].xcor()
            new_y = self.tim_list[segment - 1].ycor()
            self.tim_list[segment].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color("green")
        self.speed(20)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-340, 340)
        random_y = random.randint(-315, 315)
        self.goto(x=random_x, y=random_y)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Project_20-21_highscore_data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(0, 300)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score : {self.high_score}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("Project_20-21_highscore_data.txt", mode='w') as file:
            file.write(str(self.high_score))

