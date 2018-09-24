"""
Caliculating GCD
"""
import sys
def gcd(a,b):
    if a<0 or b<0: return -1
    if a==0: return b
    if b==0: return a
    if a<b:
        return(gcd(b-a,a))
    else:
        return(gcd(a-b,b))

print(gcd(int(sys.argv[1]),int(sys.argv[2])))
