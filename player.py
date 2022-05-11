from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.draw_middle_line()
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def draw_middle_line(self):
        self.penup()
        self.setposition(-320, -10)
        self.pencolor("white")
        self.pensize(3)
        for i in range(31):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
        self.pencolor("black")
        self.color("darkred")

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
