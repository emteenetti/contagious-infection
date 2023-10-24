from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 100, "normal")


class RestartButton(Turtle):
    def __init__(self, x_func, y_func):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(-50, 40)
        self.write("Restart", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.onclick(self, self.restart_game)
        self.x_func = x_func
        self.y_func = y_func


    def restart_game(self, x, y):
        self.x_func()
        self.y_func()
