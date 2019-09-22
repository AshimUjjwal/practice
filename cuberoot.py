def cube(a):
    a =abs(a)
    return int(round(a**(1./3))) 
a = int(input('Enter:'))
print(cube(a))

def root(v):
    v= abs(v)
    return int(round(v**(1./2)))
v=int(input("Enter:"))
print(root(v))
