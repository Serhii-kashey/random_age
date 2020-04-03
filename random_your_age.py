s=''
n=[]
print('Computer will try to find out your age \nPlease folow instruction ')
a=0
b=100
from random import randint
for i in range(b):
    t=randint(a,b)
    n.append(t)
    s=input("Please type yes if  your age is %d? or  type more or less: "%n[i])
    if s=="more":
        a=n[i]
    elif s=="less":
        b=n[i]
    else:
        print('Your age is %d'%(n[i]))
        break
#print(n)
        











        
    
