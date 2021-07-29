def fact(x):
    m=1
    for i in range(1,x):
        m=m*(i+1)
    return m
x=int(input())
print(fact(x))
