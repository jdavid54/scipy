#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     alpha
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import alpha
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
a = 3.57
mean, var, skew, kurt = alpha.stats(a, moments='mvsk')
#print(mean, var, skew, kurt)
x = np.linspace(alpha.ppf(0.01, a), alpha.ppf(0.99, a), 100)

#Display the probability density function (pdf)
ax.plot(x, alpha.pdf(x, a),'r-', lw=5, alpha=0.6, label='alpha pdf')

#Freeze the distribution and display the frozen pdf
rv = alpha(a)
ax.plot(x, rv.pdf(x), 'k-', lw=1, label='frozen pdf')

#Check accuracy of cdf and ppf
vals = alpha.ppf([0.001, 0.5, 0.999], a)
np.allclose([0.001, 0.5, 0.999], alpha.cdf(vals, a))

#Generate random numbers
r = alpha.rvs(a, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)

plt.show()