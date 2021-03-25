#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     gamma
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

a = 1.99
mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(gamma.ppf(0.01, a), gamma.ppf(0.99, a), 100)
ax.plot(x, gamma.pdf(x, a),'r-', lw=5, alpha=0.6, label='gamma pdf')

#Freeze the distribution and display the frozen pdf:
rv = gamma(a)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf
vals = gamma.ppf([0.001, 0.5, 0.999], a)
np.allclose([0.001, 0.5, 0.999], gamma.cdf(vals, a))

#Generate random numbers:
r = gamma.rvs(a, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
