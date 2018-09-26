def has_duplicates(l):
    a=sorted(l)
    n=0
    for i in a[:len(a)-2]:
        #print(i, a[i], a)
        if a[n] == a[n+1]: return True
        n=n+1
    return False

def has_dup2(l):
    i=0
    for c in l:
        i=i+1
        #print(l[i:])
        if c in l[i:]:
            return True
    return False

import sys
k=[int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])]
print(k, has_duplicates(k))
print(k, has_dup2(k))
