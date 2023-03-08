from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, game_screen):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.pendown()
        self.game_level = 1
        self.write(arg=f"Level: {self.game_level}", align="Left", move=False, font=FONT)

    def new_level(self):
        self.game_level += 1

    def clear_and_write_new_level(self):
        self.clear()
        self.write(arg=f"Level: {self.game_level}", align="Left", move=False, font=FONT)

    def write_game_over(self):
        self.goto(-60, 0)
        self.write(arg=f"GAME OVER!", align="Left", move=False, font=FONT)
