import time
from turtle import Screen
from player import Player
from movingCar import MovingCar
from scoreBoard import ScoreBoard

screen = Screen()
screen.title('The Turtle Crossing Game')
screen.bgcolor('black')
screen.setup(width=600, height=800)
screen.tracer(0)

player = Player()
car = MovingCar()
score = ScoreBoard()


screen.listen()
screen.onkey(player.move, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()
