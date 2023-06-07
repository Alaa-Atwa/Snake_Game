from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# setting screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# creating snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen to key strikes
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

# moving snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend_snake()

    # detect collision with walls
    if abs(snake.head.xcor()) > 295 or abs(snake.head.ycor() > 295):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail.
    for seg in snake.segments[1:]:  # to skip first one (the head)
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
