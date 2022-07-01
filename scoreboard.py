from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()

    def start_game(self):
        self.color("cyan")
        self.goto(0, 0)
        self.write("Press SPACE to START the game", move=True, align="center", font=("Arial", 20, "bold"))
        self.hideturtle()

    def intial(self):
        self.color("white")
        self.goto(0, 260)
        self.write(f"Scoreboard: {self.score}", move=True, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.intial()

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER.", move=True, align="center", font=("Arial", 20, "bold"))