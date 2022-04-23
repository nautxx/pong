from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()