def hi(x):
    if(x>6):
        
        raise IOError
    return x
    
try:
    print(hi(2))
except IOError:
    print('hello')


