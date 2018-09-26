def reverse_pair(s1,s2):
    if len(s1)!=len(s2): return False
    for i in range(0,int(len(s1)/2)+1):
        if s1[i]!=s2[len(s1)-i-1]: return False
    return True

import sys
print(reverse_pair(sys.argv[1],sys.argv[2]))
