def spam(i,j):
    h=i
    k=j
    for l in range(1,h):
        j=j*(k-l)
        i=i*(h-l)
    m=j/i
    return(m)
i=int(input())
j=int(input())
print(spam(i,j))
        
        
        
                                                                           
