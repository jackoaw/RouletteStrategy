import random

class Roulette:
	def __init__(self):
		pass

	# There are 35 numbers but ignoring for now	
	def colorSpin(self):
		random_float = random.random()
		chance_of_winning = .474
		if random_float <= chance_of_winning:
			return "red"
		elif random_float <= chance_of_winning*2:
			return "black"
		else:
			return "green"

	# def betOnColor(self, color_from_player):
	# 	if color_from_player == self._colorSpin():
	# 		return True
	# 	return False