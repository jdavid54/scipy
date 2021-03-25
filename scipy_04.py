#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     arcsine
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import arcsine
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = arcsine.stats(moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(arcsine.ppf(0.01), arcsine.ppf(0.99), 100)
ax.plot(x, arcsine.pdf(x),'r-', lw=5, alpha=0.6, label='arcsine pdf')

#Freeze the distribution and display the frozen pdf
rv = arcsine()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf
vals = arcsine.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], arcsine.cdf(vals))

#Generate random numbers:
r = arcsine.rvs(size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()