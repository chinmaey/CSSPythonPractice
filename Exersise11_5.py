def invert_dict(d):
    d2=dict()
    for c in d:
        if d[c] in d2: d2[d[c]]=d2[d[c]]+[c]
        else: d2[d[c]]=[c]
    return d2

def invert_dict2(d):
    d2=dict()
    for c in d:
        d2[d[c]]=d2.setdefault(d[c],[])+[c]
    return d2

a={'a': 11, 'c': 12, 'b':30, 'd':11}
print(invert_dict(a))
print(invert_dict2(a))
