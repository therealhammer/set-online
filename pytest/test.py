
class Card:
	color = 0
	number = 0
	fill = 0
	shape = 0
	def __init__ (self, color, number, fill, shape):
		self.color = color
		self.number = number
		self.fill = fill
		self.shape = shape

	def isequal(self, card):
		pass

	def isset(self, card1, card2):
		pass

n = Card(1,2,3,2)
print(n)
