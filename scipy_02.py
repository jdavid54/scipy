#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     argus
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import argus
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

chi = 1
mean, var, skew, kurt = argus.stats(chi, moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(argus.ppf(0.01, chi), argus.ppf(0.99, chi), 100)
ax.plot(x, argus.pdf(x, chi),'r-', lw=5, alpha=0.6, label='argus pdf')

#Freeze the distribution and display the frozen pdf:
rv = argus(chi)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf
vals = argus.ppf([0.001, 0.5, 0.999], chi)
np.allclose([0.001, 0.5, 0.999], argus.cdf(vals, chi))

#Generate random numbers:
r = argus.rvs(chi, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
