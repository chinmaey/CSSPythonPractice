def reverse_lookup(d,v):
    for c in d:
        if d[c]==v:return c
    return -1

def reverse_lookupList(d,v):
    i=0
    a=[]
    for c in d:
        if d[c]==v: a=a+[c]
    return a
a={'a': 11, 'c': 12, 'b':30, 'd':11}
"""s=''
while 1:
    s=input().strip()
    if s == 'done': break
    key=s[:s.find(' ')].strip()
    val=int(s[s.find(' ')+1:].strip())
    a[key]=val
"""
print(a)
print(111,reverse_lookup(a,111))
print(111,reverse_lookupList(a,111))
