#-------------------------------------------------------------------------------
# Name:        scipy integration example
# Purpose:     https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
#
'''
help(integrate)
 Methods for Integrating Functions given function object.

   quad          -- General purpose integration.
   dblquad       -- General purpose double integration.
   tplquad       -- General purpose triple integration.
   fixed_quad    -- Integrate func(x) using Gaussian quadrature of order n.
   quadrature    -- Integrate with given tolerance using Gaussian quadrature.
   romberg       -- Integrate func using Romberg integration.

 Methods for Integrating Functions given fixed samples.

   trapz         -- Use trapezoidal rule to compute integral from samples.
   cumtrapz      -- Use trapezoidal rule to cumulatively compute integral.
   simps         -- Use Simpson's rule to compute integral from samples.
   romb          -- Use Romberg Integration to compute integral from
                    (2**k + 1) evenly-spaced samples.

   See the special module's orthogonal polynomials (special) for Gaussian
      quadrature roots and weights for other weighting factors and regions.

 Interface to numerical integrators of ODE systems.

   odeint        -- General integration of ordinary differential equations.
   ode           -- Integrate ODE using VODE and ZVODE routines.
'''
# Author:      Jean
#
# Created:     16/10/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import scipy.integrate as integrate
import scipy.special as special

'''
The first argument to quad is a “callable” Python object
(i.e. a function, method, or class instance).
Notice the use of a lambda- function in this case as the argument.
The next two arguments are the limits of integration.
The return value is a tuple, with
the first element holding the estimated value of the integral
and the second element holding an upper bound on the error.
'''
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
print(result)
#(1.1178179380783249, 7.8663172481899801e-09)

from numpy import sqrt, sin, cos, pi
I = sqrt(2/pi)*(18.0/27*sqrt(2)*cos(4.5) - 4.0/27*sqrt(2)*sin(4.5) +sqrt(2*pi) * special.fresnel(3/sqrt(pi))[0])
print(I)
#1.117817938088701

print(abs(result[0]-I))
#1.03761443881e-11

from scipy.integrate import quad
def integrand(x, a, b):
    return a*x**2 + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)
#(1.6666666666666667, 1.8503717077085944e-14)
print('################################"')
#from scipy.integrate import quad
def integrand(t, n, x):
    return np.exp(-x*t) / t**n

# intégral de 1 à +inf
def expint(n, x):
    return quad(integrand, 1, np.inf, args=(n, x))[0]

vec_expint = np.vectorize(expint)
print(vec_expint(3, np.arange(1.0, 4.0, 0.5)))
#array([ 0.1097,  0.0567,  0.0301,  0.0163,  0.0089,  0.0049])

print(special.expn(3, np.arange(1.0,4.0,0.5)))
#array([ 0.1097,  0.0567,  0.0301,  0.0163,  0.0089,  0.0049])

from scipy.integrate import quad, dblquad
def I(n):
    return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)

print(I(4))
#(0.2500000000043577, 1.29830334693681e-08)
print(I(3))
#(0.33333333325010883, 1.3888461883425516e-08)
print(I(2))
#(0.4999999999985751, 1.3894083651858995e-08)

area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)
print(area)
#(0.010416666666666668, 1.1564823173178715e-16)

N = 5
def f(t, x):
    return np.exp(-x*t) / t**N

print(integrate.nquad(f, [[1, np.inf],[0, np.inf]]))
#(0.20000000000002294, 1.2239614263187945e-08)

def f(x, y):
    return x*y

def bounds_y():
    return [0, 0.5]

def bounds_x(y):
    return [0, 1-2*y]

print(integrate.nquad(f, [bounds_x, bounds_y]))
#(0.010416666666666668, 4.101620128472366e-16)

def f1(x):
    return x**2

def f2(x):
    return x**3

x = np.array([1,3,4])
y1 = f1(x)

from scipy.integrate import simps
I1 = simps(y1, x)
print(I1)
#21.0

y2 = f2(x)
I2 = integrate.simps(y2, x)
print(I2)
#61.5

