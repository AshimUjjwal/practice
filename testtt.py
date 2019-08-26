a= str(input("Enter the string:"))
b= int(input("Enter the number:"))

for i in range(len(a)):
    print(a[i+b])
    b-=2
    
