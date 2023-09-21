from turtle import Turtle
with open("high.txt", "r+") as file:
	contents = int(file.read())



class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(0, 270)
		self.high_score = contents
		self.update_score()



	def reset(self):
		if self.score > self.high_score:
			file = open("high.txt", "r+")
			self.high_score = self.score
			file.write(str(self.high_score))
			file.close()
		self.score = 0
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("ariel", 14, "normal"))

	# def game_over(self):
	# 	self.goto(0, 0)
	# 	self.clear()
	# 	self.write("Game over!", align="center", font=("Courier", 14, "normal"))
	def get_points(self):
		self.score += 1
		self.update_score()





