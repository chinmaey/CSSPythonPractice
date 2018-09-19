import sys
def right_justify(s):
    #t="                                                                      "
    #while i < 70-len(s):
    #for i in range(70-len(s)):
    #    t=t+' '
    #t=t[:70-len(s)]+s
    t=' '*(70-len(s))+s
    #t=t+s
    return t

print("%s" %right_justify(sys.argv[1]))
