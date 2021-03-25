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
import numpy as np
from scipy import linalg

equation = np.array([[1, 5], [3, 7]])
solution = np.array([[6], [9]])

roots = linalg.solve(equation, solution)

print("Found the roots:")
print(roots)

print("\n Dot product should be zero if the solutions are correct:")
print(equation.dot(roots) - solution)