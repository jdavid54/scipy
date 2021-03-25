#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     betaprime
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import betaprime
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

a, b = 5, 6
mean, var, skew, kurt = betaprime.stats(a, b, moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(betaprime.ppf(0.01, a, b), betaprime.ppf(0.99, a, b), 100)
ax.plot(x, betaprime.pdf(x, a, b),'r-', lw=5, alpha=0.6, label='betaprime pdf')

#Freeze the distribution and display the frozen pdf
rv = betaprime(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Check accuracy of cdf and ppf
vals = betaprime.ppf([0.001, 0.5, 0.999], a, b)
np.allclose([0.001, 0.5, 0.999], betaprime.cdf(vals, a, b))

#Generate random numbers:
r = betaprime.rvs(a, b, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()