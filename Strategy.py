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

	def start(self, rouletteTable, maxSpins, numberOfSimulations, stratName):
		success_count = 0
		fail_count = 0
		x_axis = []
		for s in range(0, maxSpins):
			x_axis.append(str(s))
		lg = _LineGraph(x_axis, stratName)
		avg_end_value_wo_0 = 0
		avg_end_value_w_0 = 0
		for k in range(0, numberOfSimulations):
			currentMoneyValues = [0]*maxSpins
			fail = False
			for i in range(0, maxSpins):

				if not self.spin(rouletteTable):
					currentMoneyValues[i] = (self.currentMoney)
					fail = True
					break

				currentMoneyValues[i] = (self.currentMoney)

			lg.plot("Simulation %i" % k, currentMoneyValues)
			lg.changeColor()
			if(self.currentMoney > self.startingBet):
				success_count += 1
			self.currentMoney = self.startingMoney
			self.currentBet = self.startingBet
			avg_end_value_w_0 += currentMoneyValues[i]
			if not fail: 
				avg_end_value_wo_0 += currentMoneyValues[i]
			else:
				fail_count += 1
		print("Ran %i simulations, spinning %i times, starting with %i, starting bet: %i"%(numberOfSimulations, maxSpins, self.startingMoney, self.startingBet))
		avg_end_value_w_0 = avg_end_value_w_0/numberOfSimulations
		avg_end_value_wo_0 = avg_end_value_wo_0/(numberOfSimulations-fail_count)
		print("Average money at the end including failures: %i"%avg_end_value_w_0)
		print("Average money at the end not including failures: %i"%avg_end_value_wo_0)
		print("Successfullness of this strategy over %i runs is %f%%" %(numberOfSimulations, (success_count/numberOfSimulations)*100))
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

	def start(self, rouletteTable, maxSpins, numberOfSimulations, stratName):
		super().start(rouletteTable, maxSpins, numberOfSimulations, stratName)

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