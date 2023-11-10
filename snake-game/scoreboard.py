from turtle import Turtle
from snake import Snake

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.gameOn = True

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.gameOn = False
        self.write("GameOver, Click to Restart", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def restart_game(self):
    #     self.clear()
    #     self.score = 0
    #     self.update_scoreboard()
    #     self.gameOn = True
    #     Snake().restart_game()
