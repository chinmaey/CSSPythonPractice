def any_lowercase1(s):
    """checks only first char"""
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """error method called for const char"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """checks only for the last character"""
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Returns correct value of flag to check if the lower case exist"""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Checks if all lowercase are present"""
    for c in s:
        if not c.islower():
            return False
    return True
import sys
str=sys.argv[1]
print("any_lowercase1",any_lowercase1(str))
print("any_lowercase2",any_lowercase2(str))
print("any_lowercase3",any_lowercase3(str))
print("any_lowercase4",any_lowercase4(str))
print("any_lowercase5",any_lowercase5(str))
