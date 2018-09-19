def do_twice(f,v):
    f(v)
    f(v)

def print_spam(s):
    print (s)

def print_twice(st):
    print((st+'\n')*2)
    #print(st)

def do_four(f,v):
    for i in range(4):
        f(v)

do_four(print,'spam')
#do_twice(print_spam,'test')
