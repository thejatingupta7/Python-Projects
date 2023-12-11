from turtle import Turtle
POSITION = [(-350, 0), (350, 0)]
moving1 = True


class GeneratePaddle:
    def __init__(self):
        self.paddle_list = []
        self.makeit()

    def makeit(self):
        for i in POSITION:
            self.create_paddle(i)

    def create_paddle(self, i):
        tim = Turtle(shape="square")
        tim.pu()
        tim.speed(20)
        tim.goto(i)
        tim.right(90)
        tim.speed(2)
        tim.turtlesize(stretch_len=5)
        tim.color("white")
        self.paddle_list.append(tim)


    def w(self):
        self.paddle_list[0].bk(20)
    def s(self):
        self.paddle_list[0].fd(20)
    def up(self):
        self.paddle_list[1].bk(20)
    def down(self):
        self.paddle_list[1].fd(20)


class Ball(Turtle, GeneratePaddle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_hit(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.velocity *= 0.9

    def reset_ball(self):
        self.hideturtle()
        self.goto(0, 0)
        self.velocity = 0.1
        self.showturtle()
        self.paddle_hit()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align='center', font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score2, align='center', font=("Courier", 80, "normal"))

    def point_1(self):
        self.score1 += 1
        self.update_score()
    def point_2(self):
        self.score2 += 1
        self.update_score()