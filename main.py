from turtle import Screen

from scoreboard import Score

from food import Food

from snake import Snake

import time

score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

sap = Snake()
screen.listen()
screen.onkey(sap.up, "Up")
screen.onkey(sap.down, "Down")
screen.onkey(sap.left, "Left")
screen.onkey(sap.right, "Right")


food = Food()
score = Score()

game_is_on = True

while game_is_on:

	screen.update()
	time.sleep(0.07)
	sap.move()
	if sap.head.distance(food) < 15:
		print("nom nom nom")
		food.refresh()
		sap.add_segment()
		score.get_points()
		#collision

	for seg in sap.segments[1:]:
		if sap.head.distance(seg) < 10:
			# game_is_on = False
			# score.game_over()
			score.reset()
			sap.snake_reset()
			break

	if abs(sap.head.xcor()) > 290 or abs(sap.head.ycor()) > 290:
		score.reset()
		sap.snake_reset()
		# game_is_on = False
		# score.game_over()





















screen.exitonclick()