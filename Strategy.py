import random
import matplotlib.pyplot as plt
import matplotlib as mpl

class Strategy:
	def __init__(self, startingMoney, startingBet, maxBet):
		self.currentBet = startingBet
		self.startingBet = startingBet
		self.currentMoney = startingMoney
		self.startingMoney = startingMoney
		self.maxBet = maxBet

	def _onLoss(self):
		pass


	def _onWin(self):
		pass


	def spin(self, rouletteTable):
		pass

	def start(self, rouletteTable, maxSpins, numberOfSimulations):
		x_axis = []
		for s in range(0, maxSpins):
			x_axis.append(str(s))
		lg = _LineGraph(x_axis, "Double on Loss Strategy")

		for k in range(0, numberOfSimulations):
			currentMoneyValues = []
			for i in range(0, maxSpins):

				if not self.spin(rouletteTable):
					currentMoneyValues.append(self.currentMoney)
					continue	

				currentMoneyValues.append(self.currentMoney)

			lg.plot("Simulation %i" % k, currentMoneyValues)
			lg.changeColor()
			self.currentMoney = self.startingMoney
			self.currentBet = self.startingBet
		lg.show()

	def _printPosition(self):
		print("You have $%i" % self.currentMoney)
		print("Your bet is now $%i" % self.currentBet)


class DoubleOnLoss(Strategy):
	
	def __init__(self, startingMoney, startingBet, maxBet):
		super().__init__(startingMoney, startingBet, maxBet)

	def _onLoss(self):
		self.currentMoney -= self.currentBet
		self.currentBet *= 2
		if self.currentBet > self.currentMoney:
			self.currentBet = self.startingBet
		# print("Loss")

	def _onWin(self):
		self.currentMoney += self.currentBet*2
		self.currentBet = self.startingBet
		# print("Win")


	def spin(self, rouletteTable):
		if self.currentMoney < self.startingBet: 
			# print("You lost all your money")
			return False

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
			self.currentBet = self.startingBet

		# self._printPosition()
		return True

	def start(self, rouletteTable, maxSpins, numberOfSimulations):
		super().start(rouletteTable, maxSpins, numberOfSimulations)


class _LineGraph:

	def __init__(self, x_axis, title):
		self.x_axis = x_axis
		self.title = title
		self.color = (0,0,0)
		self.x_len = len(x_axis)

		mpl.style.use('seaborn')


	# Change the color for each new symbol
	def changeColor(self):
		old_color = int(self.color[1])
		r = random.random()
		g = random.random()
		b = random.random()
		self.color = (r,g,b)
		

	def plot(self, value_title, value_array):
		if len(value_array) == self.x_len:
			plt.plot(self.x_axis, value_array, color=self.color, label=value_title)

	def show(self):
		plt.legend()
		plt.show()