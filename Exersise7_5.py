"""

"""
import math

def estimate_pi ():
    T=float(0)
    k=0
    S=float(0)
    while 1:
        T=(math.factorial(4*k)*(1103+26390*k))/((math.factorial(k)**4)*(396**(4*k)))
        print(k)
        print("T", T)
        if T < 1e-15:
            return(9801/(2*math.sqrt(2)*S))
        else:
            S=S+T
            print(S)
            k=k+1
            print("k.")

print(math.factorial(0))
print("Estimate_pi:",estimate_pi())
print("math_pi:",math.pi)
