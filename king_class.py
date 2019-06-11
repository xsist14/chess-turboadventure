# moves one space in any direction

class King:
	color = 'white'
	starting_position = 'e1'
	row = 1
	column = 'e'

	def move_forward(self):
		self.row+=1
		print "The king moved forward to column "
		print self.row

	def move_back(self):
		self.row-=1
		print "The king moved back to column "
		print self.row


