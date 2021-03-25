#-------------------------------------------------------------------------------
# Name:        Fourier Transformations
# Purpose:
#
# Author:      Jean
#
# Created:     22/03/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
from scipy.fftpack import fft

# Number of sample points
N = 500

# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.cos(50.0 * 2.0* np.pi * x) + 0.5 * np.cos(80.0 * 2.0 * np.pi * x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0 * T), N//2)

# matplotlib for plotting purposes
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.grid()
plt.show()