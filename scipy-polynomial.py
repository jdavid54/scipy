#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     22/03/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from numpy import poly1d

first_polynomial = poly1d([3, 4, 7])
print(first_polynomial,'\n')

print("Polynomial Square: ")
print(first_polynomial * first_polynomial,'\n')

print("Derivative of Polynomial: ")
print(first_polynomial.deriv(),'\n')

print("Solving the Polynomial: ")
print(first_polynomial(3),'\n')

print("Integrating the Polynomial: ")
print(first_polynomial.integ(1),'\n')