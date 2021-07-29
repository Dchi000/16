a=4;
def cas(b):
    global eggs
    eggs=5
    return eggs
def ss():
    eggs=8
    print(eggs,end=" ")
b=1
b=cas(b)
ss()
print(b,end=" ")
print(a,end=" ")
