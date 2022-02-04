STARTING_POSITION = (0, -280)
MOVE_DIST = 10
FINISH_LINE_Y = 280

from turtle import Turtle





class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move(self):
        new_y = self.ycor()+MOVE_DIST
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            self.go_to_start()
            return True
        else:
            return False





