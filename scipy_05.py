#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     beta
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

a, b = 2.31, 0.627
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
ax.plot(x, beta.pdf(x, a, b),'r-', lw=5, alpha=0.6, label='beta pdf')

#Freeze the distribution and display the frozen pdf
rv = beta(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Check accuracy of cdf and ppf
vals = beta.ppf([0.001, 0.5, 0.999], a, b)
np.allclose([0.001, 0.5, 0.999], beta.cdf(vals, a, b))

#Generate random numbers:
r = beta.rvs(a, b, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()