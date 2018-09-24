"""Practice Functions and stack
"""

def f1(a):
    """ Test Int pass by value/referene
    """
    print(type(a))
    print("f1 in- %d"%a)
    a = a + 1
    print("f1 ret- %d"%a)

def f2(a):
    """ Test char pass by value/referene
    """
    print(type(a))
    print("f2 in- %c"%a)
    a = str(a + 1)
    print("f2 ret- %c"%a)

def f3(a):
    """ Test list pass by value/referene
    """
    print(type(a))
    print("f3 in-", a)
    a[0] = a[0] + 1
    print("f3 ret-", a)
    print(type(a))

x="hello"
y=["world"]
b=[0,1]
z=x+y
print(z)
print("main - Init ")
print(b)
f3(b)
print("main - Ret ",b)
