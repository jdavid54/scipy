#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     gengamma
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import gengamma
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

a, c = 4.42, -3.12
mean, var, skew, kurt = gengamma.stats(a, c, moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(gengamma.ppf(0.01, a, c), gengamma.ppf(0.99, a, c), 100)
ax.plot(x, gengamma.pdf(x, a, c),'r-', lw=5, alpha=0.6, label='gengamma pdf')

#Freeze the distribution and display the frozen pdf:
rv = gengamma(a, c)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf
vals = gengamma.ppf([0.001, 0.5, 0.999], a, c)
np.allclose([0.001, 0.5, 0.999], gengamma.cdf(vals, a, c))

#Generate random numbers:
r = gengamma.rvs(a, c, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
