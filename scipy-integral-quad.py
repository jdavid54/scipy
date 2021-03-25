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
from scipy.integrate import quad

a = 2
b = 1
f=lambda x: a*x**2+b
x=np.linspace(0,10,100)
plt.plot(x,f(x))
plt.title('y=ax²+b')
plt.grid(True)
plt.show()

def integrand(x, a, b):
    return f(x)

I = quad(integrand, 0, 1, args=(a,b))
print(I)
#(1.6666666666666667, 1.8503717077085944e-14)

def integrand(t, n, x):
    return np.exp(-x*t) / t**n

# intégral de 1 à +inf
def expint(n, x):
    return quad(integrand, 1, np.inf, args=(n, x))[0]

vec_expint = np.vectorize(expint)
x=np.linspace(0,10,20)
plt.plot(x,vec_expint(2,x))
plt.title('y=expint(x)')
plt.grid(True)
plt.show()

