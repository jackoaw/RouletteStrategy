import Strategy
import Roulette

MAX_BET = 500
STARTING_MONEY = 1000
STARTING_BET = 20
MAX_SPINS = 200

NUM_SIMULATIONS = 100

table = Roulette.Roulette()

doubleOnLoss = Strategy.DoubleOnLoss(STARTING_MONEY,STARTING_BET,MAX_BET)
doubleOnLoss.start(table, MAX_SPINS, NUM_SIMULATIONS, "Double on Loss Strategy")