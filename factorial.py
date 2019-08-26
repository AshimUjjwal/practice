#Method 1

from functools import reduce
a=int(input('Enter:'))
print(reduce(lambda x,y:x*y,list(range(1,a+1)) if a>0 else 1))

#Method 2

def fac(x):
    return 1 if x==0 or x==1 else x*fac(x-1)
x=int(input('Enter:'))
print(fac(x))

#Method 3

y=int(input('Enter:'))

f=1
p=1

if y==0 or y==1:
    print(p)

else:
    for i in range(1,y+1):
        f=f*i
        print(f)


       







                        
