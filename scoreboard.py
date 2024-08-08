from turtle import Turtle
FONT = ('Arial', 35, 'normal')


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        if self.xcor() == -30:
            self.align = "left"
        elif self.xcor() == 30:
            self.align = "right"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=self.align, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
