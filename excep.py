x = int(input('Enter:'))
y = int(input('Enter:'))



try:
    c=x/y


except TypeError:
    print('oops!! error')


except ZeroDivisionError:
    print('good!! error')

print('Hello')


def ty (age = 24,name='Sia'):
    assert(age == 24) ,'oops'
    return age

print(ty())
