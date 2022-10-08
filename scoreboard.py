from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)