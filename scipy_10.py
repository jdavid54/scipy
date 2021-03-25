#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     chi2
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

df = 55
mean, var, skew, kurt = chi2.stats(df, moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 100)
ax.plot(x, chi2.pdf(x, df),'r-', lw=5, alpha=0.6, label='chi2 pdf')

#Freeze the distribution and display the frozen pdf
rv = chi2(df)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Check accuracy of cdf and ppf
vals = chi2.ppf([0.001, 0.5, 0.999], df)
np.allclose([0.001, 0.5, 0.999], chi2.cdf(vals, df))

#Generate random numbers:
r = chi2.rvs(df, size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()