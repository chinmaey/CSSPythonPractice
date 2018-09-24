"""
def rotateRight(s,n):
    n=n%len(s)
    return(s[len(s)-n:]+s[:len(s)-n])

def rotateLeft(s,n):
    n=n%len(s)
    return(s[n:]+s[:n])

import sys
st=sys.argv[1]
ln=int(sys.argv[2])
print("RotateLeft %d:"%ln, rotateLeft(st,ln))
print("RotateRight %d:"%ln,rotateRight(st,ln))
"""
def rotate_word(s,n):
    r=''
    for c in s:
        if c >= 'a': b=ord('a')
        else: b=ord('A')
        r=r+chr(((ord(c)-b+n)%26)+b)
    return r
import sys
print(rotate_word(sys.argv[1],int(sys.argv[2])))
#print(ord('A'),chr(66))
