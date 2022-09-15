def pali (a)
    l = len(a)
    k =true
    i =0
    while(i<=l/2)
        if(a[i]==a[l])
            l=-1
            i+=1
        return False
    return True

print(pali(111))
    
    