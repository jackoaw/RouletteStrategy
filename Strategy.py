import random
import matplotlib.pyplot as plt
import matplotlib as mpl

class Strategy:
	def __init__(self, startingMoney, startingBet, maxBet):
		self.currentBet = startingBet
		self.startingBet = startingBet
		self.currentMoney = startingMoney
		self.maxBet = maxBet

	def _onLoss(self):
		pass

	def _onWin(self):
		pass

	def start(self, rouletteTable):
		pass

	def _printPosition(self):
		print("You have $%i" % self.currentMoney)
		print("Your bet is now $%i" % self.currentBet)


class DoubleOnLoss(Strategy):
	def __init__(self, startingMoney, startingBet, maxBet):
		super().__init__(startingMoney, startingBet, maxBet)

	def _onLoss(self):
		self.currentMoney -= self.currentBet
		self.currentBet *= 2
		print("Loss")

	def _onWin(self):
		self.currentMoney += self.currentBet*2
		self.currentBet = self.startingBet
		print("Win")

	def start(self, rouletteTable, maxSpins, numberOfSimulations):
		for k in range(0, numberOfSimulations):
			for i in range(0, maxSpins):
				if self.currentMoney < 0: 
					print("You lost all your money")

				random_float = random.random()
				chance_of_winning = .5
				if random_float <= chance_of_winning:
					colorBet = "red"
				else:
					colorBet = "black"

				if rouletteTable.betOnColor(colorBet):
					self._onWin()
				else:
					self._onLoss()

				if self.currentBet > self.maxBet:
					currentBet = self.startingBet

				self._printPosition()

	def plot(self):
		pass


class _LineGraph:

	def __init__(self, x_axis, title):
		self.x_axis = x_axis
		self.title = title
		self.color = "C0"
		self.x_len = len(x_axis)

		mpl.style.use('seaborn')


	# Change the color for each new symbol
	def changeColor(self):
		old_color = int(self.color[1])
		self.color = "C" + str(old_color + 1)
		

	def plot(self, symbol, diff_array):
		if len(diff_array) == self.x_len:
			plt.plot(self.x_axis, diff_array, color=self.color, label=symbol)

	def show(self):
		plt.legend()
		plt.show()