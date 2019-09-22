x = int(input("Enter:"))
def fib(x):
    a,b=0,1
    while a < x:
        print(a, end = ' ')
        a,b=b,a+b
    print()
    return
fib(x)
    
  


