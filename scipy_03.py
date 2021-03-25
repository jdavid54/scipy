#-------------------------------------------------------------------------------
# Name:        scipy
# Purpose:     anglit
#
# Author:      Jean
#
# Created:     27/08/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import anglit
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = anglit.stats(moments='mvsk')
#Display the probability density function (pdf)
x = np.linspace(anglit.ppf(0.01), anglit.ppf(0.99), 100)
ax.plot(x, anglit.pdf(x),'r-', lw=5, alpha=0.6, label='anglit pdf')

#Freeze the distribution and display the frozen pdf
rv = anglit()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#Check accuracy of cdf and ppf
vals = anglit.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], anglit.cdf(vals))

#Generate random numbers:
r = anglit.rvs(size=1000)

#And compare the histogram
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()