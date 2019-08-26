class cat:
    a=4+6

b=cat()
print(b.a)


class person:
    def __init__(self,name,age):
        
        
        self.name=name
        self.age=age

a=person('Ashim',56)
print(a.name)
print(a.age)

class Person:
    def __init__(cow,name,age):
        cow.name=name
        cow.age=age

    def fun(cat):

            print(' My name is ' + cat.name)

x=Person('Ashim',20)
x.fun()


class Fu:
    d=9
    
    def __init__(self):
        
        print('constructer')

    #def __del__(self):
        #print('destructer')

a=Fu()

print(a.d)

import re
a=re.search(r'(\d*)(\d)','hello12334')

if a:
    print('found',a.groups(6))
else:
    print('not matched')

#match

import re
s='12345'
m=re.sub(r'(\d\d)','z',s)
print(m)
        


    
        
    
