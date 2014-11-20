
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# use matplotlib style sheet
try:
    plt.style.use('ggplot')
except:
    # version of matplotlib might not be recent
    pass

# font attributes
font = {'family' : 'serif',
        'color'  : '555555',
        'weight' : 'normal',
        'size'   : 16,
        }


fig, ax = plt.subplots(1, 1)
x = np.arange(0., 1., 0.01)

# four different parameter settings
ax.plot(x, beta.pdf(x, 1, 1), 'k-', label=r'$\alpha_0=1, \alpha_1=1$')
ax.plot(x, beta.pdf(x, 1./2, 1./2), 'r-', label=r'$\alpha_0=1/2, \alpha_1=1/2$')
ax.plot(x, beta.pdf(x, 5, 5), 'b-', label=r'$\alpha_0=5, \alpha_1=5$')
ax.plot(x, beta.pdf(x, 8, 2), 'g-', label='8,2')
ax.set_xlabel(r'Prob of Zero: $p_0$', fontdict=font)
ax.set_ylabel(r'$\rm{Beta}(p_0\vert \alpha_0, \alpha_1)$', fontdict=font)

# add legend and show
ax.legend(loc='best', frameon=False, fontsize='large')
plt.show()
