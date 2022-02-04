from turtle import Turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-280, 250)
        self.result()

    def result(self):
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.result()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align='center', font=FONT)





