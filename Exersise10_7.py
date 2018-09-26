def is_anagram(s1,s2):
    if s1==s2:
        return False
    elif len(s1)!=len(s2):
        return False
    else:
        cs1=sorted(s1)
        cs2=sorted(s2)
        if cs1!=cs2: return False
        else: return True

import sys
print(is_anagram(sys.argv[1], sys.argv[2]))
