def squareroot(a,n):
    if(a<0):
        return -1
    else:
        if(a<10):
            x=2.0
        else:
            x=6.0

        for i in range(n):
            x=(x+(a/x))/2

        return x

import sys
import math
a=float(sys.argv[1])
n=int(sys.argv[2])
print("mathsquareroot:",math.sqrt(a))
print("my squareroot :",squareroot(a,n))
