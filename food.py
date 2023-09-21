from turtle import Turtle
import random

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.shape("circle")
		self.color("blue")
		self.speed("fastest")
		self.shapesize(stretch_len=.5, stretch_wid= .5)
		self.refresh()

	def refresh(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)

