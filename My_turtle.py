""" This is my function practice.
"""
import sys
import math
sys.path.append('C:\\Users\\home\\Documents\\chinmaey-study\\software-study\Python\\swampy-2.1.5.python3\\swampy-2.1.5')

try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *

def My_square(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)

    wait_for_user()

def My_polygon(t,n,l):
    for i in range(n):
        fd(t,l)
        lt(t,360/n)

def My_Circle(t,r):
    c=2*math.pi*r
    n=100
    l=c/n
    pu(t)
    rt(t)
    fd(t,r)
    lt(t)
    pd(t)
    My_polygon(t,n,l)

if __name__=="__main__":
    world=TurtleWorld()
    bob=Turtle()
    bob.delay = 0.01
    #print(bob)

    #My_square(bob,100)
    #My_polygon(bob,1000,1)
    My_Circle(bob,100)

    wait_for_user()
