import re

def getHammingDistance(string1, string2):
    str1len = len(string1)
    str2len = len(string2)
    
    if(str1len != str2len):
        print ("Error! Strings not equal!")
        return

    inversions = 0;
    
    for index in range(0, str1len):
        if(string1[index] != string2[index]):
            inversions+=1
    
    return inversions

def countSubstrPattern(original, pattern):
    return len(re.findall(r'(?=%s)' % (pattern), original))

def isValidString(string, alphabet):
    for index in range(0, len(alphabet)):
        if alphabet[index] not in string:
            return False

    return True 

def isValidString(string, alphabet):
    for index in range(0, len(alphabet)):
        if alphabet[index] not in string:
            return False

    return True

def getSkew(string, n):
    if( n <= 0):
        return None
    g = 0
    c = 0
    for index in range(0, n):
        if(string[index] == "G"): g+=1
        elif(string[index] == "C"): c+=1

    return g-c

def getMaxSkewN(string, n):
    if( n <= 0):
        return None
    mx = getSkew(string, n)
    for index in range(1,n+1): mx = max(getSkew(string, index), mx)

    return mx

def getMinSkewN(string, n):
    if( n <= 0):
        return None
    mn = getSkew(string, n)
    for index in range(1,n+1): mn = max(getSkew(string, index), mn)

    return mn
