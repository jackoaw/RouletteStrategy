import Strategy
import Roulette

MAX_BET = 500
STARTING_MONEY = 2000
STARTING_BET = 50
MAX_SPINS = 50

NUM_SIMULATIONS = 10

table = Roulette.Roulette()

doubleOnLoss = Strategy.DoubleOnLoss(STARTING_MONEY,STARTING_BET,MAX_BET)
doubleOnLoss.start(table, MAX_SPINS, NUM_SIMULATIONS, "Double on Loss Strategy")