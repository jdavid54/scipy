#-------------------------------------------------------------------------------
# Name:        Matrix
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

my_matrix = np.matrix(np.random.random((3, 3)))
print('Matrix :',my_matrix)

la, vector = linalg.eig(my_matrix)
print('vectors : ',vector)
print('Eigvector 1 :',vector[:, 0])        # all in column 0
print('Eigvector 2 :',vector[:, 1])        # all in column 1
print('Eigvector 3 :',vector[:, 2])        # all in column 2

print('Eigvals :' ,linalg.eigvals(my_matrix))

print(linalg.det( my_matrix ))
