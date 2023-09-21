from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]


	def create_snake(self):
		initial = 0
		#Creating 3 turtles and making them included in a list called segments
		for turt in range(0, 3):
			new_turtle = Turtle("square")
			new_turtle.penup()
			new_turtle.color("white")
			new_turtle.goto(x=initial, y=0)
			initial -= 20
			self.segments.append(new_turtle)

	def snake_reset(self):
		for seg in self.segments:
			seg.goto(1000, 1000)
		self.segments.clear()
		self.create_snake()
		self.head = self.segments[0]
	def move(self):
		# for i in range(0, n-1):
		# 	all_turtles[n-1-i].goto(all_turtles[n-2-i].pos())
		#making the last segment move to the position of the second one and similarly the second one
		#to the position of the first one, so that only moving head will suffice
		for i in range(len(self.segments) - 1, 0, -1):
			self.segments[i].goto(self.segments[i - 1].pos())
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		#so that the snake can not directly turn around in the opposite direction of its current movement
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def add_segment(self):
		n = len(self.segments)-1
		new_turtle = Turtle("square")
		new_turtle.penup()
		new_turtle.color("white")
		new_turtle.goto(self.segments[n].xcor(), y=self.segments[n].ycor())
		self.segments.append(new_turtle)



