#−∗−coding:utf−8−∗−
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#dérivée de y(en tant que tableau: y[0] est la fonction, y[1] la dérivée)
def deriv(y,t):
    a=-2.0
    b=-0.1
    return np.array([y[1],a*y[0]+b*y[1]])

tps=np.linspace(0.0,10.0,1000)
#valeurs initiales de y et de sa dérivée
yinit=np.array([0.0005,0.2])
y=odeint(deriv,yinit,tps)
#print(np.array([y[1],-2.0*y[0]+-0.1*y[1]]))
#print(y)
plt.figure()
plt.plot(tps,y[:,0])
plt.xlabel('t')
plt.ylabel('y')
plt.show()
