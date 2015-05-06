
from __future__ import division, print_function
from lea import Lea

# define coin
coin = Lea.fromValFreqs(('H', 1),
                        ('T', 1))

print('Coin Distribution',
      coin,
      sep='\n')

# define six-sided die
die6 = Lea.fromValFreqs(('1', 1),
                        ('2', 1),
                        ('3', 1),
                        ('4', 1),
                        ('5', 1),
                        ('6', 1))

print('Six-sided Die Distribution',
      die6,
      sep='\n')

# define four-side die
die4 = Lea.fromValFreqs(('1', 1),
                        ('2', 1),
                        ('3', 1),
                        ('4', 1))

print('Four-sided Die Distribution',
      die4,
      sep='\n')

# construct Scenario 1
scenario1 = Lea.buildCPT((coin == 'H', die6),
                         (coin == 'T', die6))

print('Scenario 1',
      scenario1,
      sep='\n')

# construct Scenario 2
scenario2 = Lea.buildCPT((coin == 'H', die6),
                         (coin == 'T', die4))

print('Scenario 2',
      scenario2,
      sep='\n')

# get joint probs for all events
# -- scenario 1
joint_prob1 = Lea.cprod(coin, scenario1)

print('Scenario 1',
      '* Joint Probabilities',
      joint_prob1,
      sep='\n')

# get joint probs for all events
# -- scenario 2
joint_prob2 = Lea.cprod(coin, scenario2)

print('Scenario 2',
      '* Joint Probabilities',
      joint_prob2,
      sep='\n')

# prob coin given D=6, scenario 1
print("Scenario 1 -> P(C|D=6)",
      coin.given(scenario1 == '6'),
      sep='\n')

# prob coin given D=6, scenario 2
print("Scenario 2 -> P(C|D=6)",
      coin.given(scenario2 == '6'),
      sep='\n')

# prob coin given D=4, scenario 1
print("Scenario 1 -> P(C|D=4)",
      coin.given(scenario1 == '4'),
      sep='\n')

# prob coin given D=4, scenario 2
print("Scenario 2 -> P(C|D=4)",
      coin.given(scenario2 == '4'),
      sep='\n')