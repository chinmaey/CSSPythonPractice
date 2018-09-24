"""Write a function named check_fermat that takes four parameters—a, b, c and n—and that
checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
an + bn = cn
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
"""
import sys

def check_fermat(a,b,c,n):
    """ a , b, c - numbers
    n - power
    Check a**n+b**n=c**n can not true for n>2 """

    if n>2:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
n=int(input("Enter n:"))
#check_fermat(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
check_fermat(a,b,c,n)
