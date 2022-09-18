from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# TODO 1. Create a snake body,

snake = Snake()
food = Food()
score = Scoreboard()

# TODO 2. Move the snake,
# TODO 3. How to control the snake
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


# TODO 4. Detect collision with food
# TODO 5. Create a scoreboard

    if snake.head.distance(food) < 15:
        food.new_location()
        snake.new_segment()
        score.recalc_score()

# TODO 6. Detect collision with wall.

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        # from the course if snake.head.distance(segment) < 10:
        if segment.xcor() == snake.head.xcor() and segment.ycor() == snake.head.ycor():
            game_is_on = False
            score.game_over()

# TODO 7. Detect collision with tail.


screen.exitonclick()