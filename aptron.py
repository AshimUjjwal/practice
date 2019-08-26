list1=['Tea','Coffee','Biscuit']

a={'Tea':6,'Coffee':8,'Biscuit':10}

prices={'Tea':2,'Coffee':4,'Biscuit':5}

def bill(brew,a):
    count =0
    for i in brew:
        tot = a[i] * prices[i]
        print(i,tot)
        #print(tot)
        count+=tot
    return count
a=int(input('Enter:'))
prices=int(input('Enter:'))

print(bill(a,prices))
   
