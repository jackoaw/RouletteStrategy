# RouletteStrategy

The goal of this project is to demonstrate the "" strategy. You can visualize your money over the runs and simulations with this program that virtually emulates that strategy. In the go.py file you have the following configurations:

MAX_BET = 500 (the maximum ammount you are allowed to bet before reseting your bet to STARTING_BET)

STARTING_MONEY = 10000 (The ammount of money you start with)

STARTING_BET = 20 (The bet you will start off with, doubling on each loss until MAX_BET)

MAX_SPINS = 100 (The number of spins you will perform if you're cash doesn't go to 0)

NUM_SIMULATIONS = 10 (The number of simulations to do with the above values)


Please change them accordingly for what you'd like to visualize.

## Run Instructions 

`pip install -r requirements.txt`

`python go.py`

## Future considerations

- Making a config file outside of go.py
