def computeLongestPalindromeLength(arr):

    def pali(b):
        a = str(b)
        l = len(a)-1
        i = 0
        while(i<=l):
            if a[i]!=a[l]:
                return False
            i+=1
            l-=1
        return True
        
    max = 0
    for s in arr:
        k = str(s)
        if(pali(k)==True):
            if len(k) > max:
                max = len(k)
    return max


arr = [1121]
print(computeLongestPalindromeLength(arr))