from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reached_top_edge(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True


