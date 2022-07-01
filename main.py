from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


score.start_game()


def game():
    score.clear()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        score.intial()
        # Detecting collision with food
        if snake.snake_head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update()

        # Detecting collision with wall
        if snake.snake_head.xcor() > 297 or snake.snake_head.xcor() < -297 or snake.snake_head.ycor() > 297 or snake.snake_head.ycor() < -297:
            score.game_over()
            game_is_on = False

        # Detecting collision with own tail
        for segment in snake.segments[1:]:
            if snake.snake_head.distance(segment) < 10:
                score.game_over()
                game_is_on = False


screen.onkey(key="space", fun=game)

screen.exitonclick()
