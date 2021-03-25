# −∗− c odin g : u t f −8 −∗−
from numpy import *
from scipy import integrate

def fn(x) :
#fonction à integrer
    return 4.0 / (1+ (x-3)*(x-3))

def main() :
    print (" par Scipy : " , integrate.quad( fn , 0 , 5 ))
    print (" Romberg par Scipy : " , integrate.romberg ( fn , 0 , 5 ))
    #Subdivision de l’intervalle par pas régulier
    x = linspace ( 0 , 5 , 1000 )
    y=fn(x)
    print (" trapezes par Spicy " , integrate.trapz( y , x , dx = 0.1 ))

main ()
