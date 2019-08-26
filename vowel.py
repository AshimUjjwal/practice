
string = str(input('Enter:'))
string = string.lower()

vowels = 'aeiou'

count = {}.fromkeys(vowels,0)

for i in string:
    if i in count:
        
        count[i] +=1
        


print(count)
