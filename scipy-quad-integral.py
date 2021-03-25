#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     03/11/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt

'''
The first argument to quad is a “callable” Python object
(i.e. a function, method, or class instance).
Notice the use of a lambda- function in this case as the argument.
The next two arguments are the limits of integration.
The return value is a tuple, with
the first element holding the estimated value of the integral
and the second element holding an upper bound on the error.
'''

x=np.linspace(0,10,100)
jv=lambda x: special.jv(2.5,x)
plt.plot(x,jv(x))
plt.show()

from numpy import sqrt, sin, cos, pi
f=special.fresnel(3/sqrt(pi))
print(f)
#plot the function fresnel
f1=lambda x: special.fresnel(x/sqrt(pi))[0]
f2=lambda x: special.fresnel(x/sqrt(pi))[1]
plt.plot(x,f1(x))
plt.plot(x,f2(x))
plt.show()
