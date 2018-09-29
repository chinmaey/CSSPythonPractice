def has_dup(l):
    d=dict()
    for i in l:
        if i in d: return True
    return False

import sys
k=[int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])]
print(k, has_dup(k))
