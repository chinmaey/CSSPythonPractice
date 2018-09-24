import sys
#import str

def parse_line(s):
    w=e=0
    s=str.rstrip(s)
    while len(s)>0:
        w=w+1
        sp=s.find(' ')
        if(sp>=0):
            if('e' in s[:sp]): e=e+1
            s=s[sp+1:]
        else:
            if('e' in s): e=e+1
            break
    return (100*e/w)

try:
    f=open(".\\a.txt","rt")
except FileNotFoundError:
    print("File not found error!")
else:
    st=''
    for ln in f:
        st=st+ln
    print(parse_line(st)," %")
    f.close()
finally:
    print("Done!")
