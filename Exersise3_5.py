import sys
def print_rowCol(r,c):
    #s1='+----+----+\n'
    s1=('+'+'-'*4)*c
    s2=('|'+' '*4)*c
    #print((s1+'+\n'+(s2+'|\n')*4)*2+s1+'+\n')
    print((s1+'+\n'+(s2+'|\n')*4)*r+s1+'+\n')

print_rowCol(int(sys.argv[1]),int(sys.argv[2]))
