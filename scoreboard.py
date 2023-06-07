from turtle import Turtle

FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = file.read()
        self.score = 0
        self.color('yellow')
        self.penup()
        self.setposition(-40, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score=  {self.score}  High Score= {self.high_score}", font=FONT,  align="center")

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
