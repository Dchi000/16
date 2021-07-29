def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    elif number%2!=0:
        print(number*3+1)
        return number*3+1
m=int(input("Enter number:"))
while m>1:
    m=collatz(m)

    
    
        
