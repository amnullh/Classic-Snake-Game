from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food.
    if snake.all_segments[0].distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.all_segments[0].xcor() > 290 or snake.all_segments[0].xcor() < -290 or snake.all_segments[0].ycor() > 290 \
            or snake.all_segments[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #  Detect collision with tail.
    for segment in snake.all_segments[1:]:
        # if segment == snake.all_segments[0]:
        #     pass
        if snake.all_segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()