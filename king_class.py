# moves one space in any direction
from board_class import *

class King:
	board_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
	color = 'white'
	starting_position = 'e1'
	row = 1
	column = 'e'
	movement = 4

	def move_forward(self):
		if self.row >= 8:
			self.row = 8
		else:
			self.row+=1


	def move_back(self):
		if self.row <= 1:
			self.row = 1
		else:
			self.row-=1

	def move_left(self):
		self.movement -= 1

	def move_right(self):
		self.movement += 1


	def get_king_position(self):
		print board_columns[movement]
		print self.row



