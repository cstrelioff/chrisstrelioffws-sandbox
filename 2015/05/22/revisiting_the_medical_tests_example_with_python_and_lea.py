
from __future__ import division, print_function
from lea import Lea

# define cancer dist
cancer = Lea.fromValFreqs(('yes', 1),
                          ('no',  99))

print('\nCancer Distribution',
      'P(C)',
      cancer.asPct(),
      sep='\n')

# prob for mamm given cancer == yes
mamm_g_cancer = Lea.fromValFreqs(('pos', 80),
                                 ('neg', 20))

print('\nProb for mammogram given cancer',
      'P(M|C=yes)',
      mamm_g_cancer.asPct(),
      sep='\n')

# prob for mamm given cancer == no
mamm_g_no_cancer = Lea.fromValFreqs(('pos', 96),
                                    ('neg', 1000-96))

print('\nProb for mammogram given NO cancer',
      'P(M|C=no)',
      mamm_g_no_cancer.asPct(),
      sep='\n')

# conditional probability table
mammograms = Lea.buildCPT((cancer == 'yes', mamm_g_cancer),
                          (cancer == 'no', mamm_g_no_cancer))

print('\nMammograms',
      'P(M)',
      mammograms.asPct(),
      sep='\n')

# get joint probs for all events
joint_probs = Lea.cprod(mammograms, cancer)

print('\nJoint Probabilities',
      'P(M, C)',
      joint_probs.asPct(),
      sep='\n')

# prob cancer GIVEN mammogram==pos
print('\nThe Answer',
      'P(C|M=pos)',
      cancer.given(mammograms == 'pos').asPct(),
      sep='\n')

# prob cancer GIVEN mammogram==neg
print('\nExtra Infor',
      'P(C|M=neg)',
      cancer.given(mammograms == 'neg').asPct(),
      sep='\n')