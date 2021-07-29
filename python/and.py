def thing(spam):
    for i in spam[0:-1]:
        print(i+", ",end="")
    spam.insert(-1,"and")
    for i in spam[-2:]:
        print(i+' ',end="")
    
spam=[]
name=input()
while name!="":
    spam=spam+[name]
    name=input()
thing(spam)
    
