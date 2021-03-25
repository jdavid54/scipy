#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     halfcauchy
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import halfcauchy
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = halfcauchy.stats(moments='mvsk')
#print(mean, var, skew, kurt)
x = np.linspace(halfcauchy.ppf(0.01), halfcauchy.ppf(0.99), 100)

#Display the probability density function (pdf)
ax.plot(x, halfcauchy.pdf(x),'r-', lw=5, alpha=0.6, label='halfcauchy pdf')

#Freeze the distribution and display the frozen pdf
rv = halfcauchy()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Check accuracy of cdf and ppf
vals = halfcauchy.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], halfcauchy.cdf(vals))

#Generate random numbers
r = halfcauchy.rvs(size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)

plt.show()