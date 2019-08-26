def kelvintofarenheit(farenheit):
    assert(farenheit>=0)
    kelvin=farenheit
    farenheit=1.8*(kelvin-273)+32
    return farenheit
print('Kelvin To Farenheit->')
farenheit=int(input('Enter temp:'))
print(kelvintofarenheit(farenheit))

'''def farenheittokelvin(kelvin):
    assert(kelvin>=0)
    
    kelvin = 0.5*(farenheit-32)+273
    return kelvin
print('Farenheit To Kelvin->')
kelvin=int(input('Enter Temp:'))
print(farenheittokelvin(kelvin))


def kelvintocelsius(celsius):
    assert(celsius>=0)
    kelvin =celsius
    celsius = kelvin - 273
    return celsius
print('Kelvin To Celsius->')
celsius =int(input('Enter temp:'))
print(kelvintocelsius(celsius));print('° C')

def celsiustokelvin(kelvin):
    assert(kelvin>=0)
    #celsius=kelvin
    kelvin = celsius + 273
    return kelvin
print('Celsius To Kelvin->')
kelvin = int(input('Enter temp:'))
print(celsiustokelvin(kelvin))
print('K')

def celsiustofarenheit(farenheit):
    assert(farenheit>=0)
    farenheit= 9/5*(celsius) + 32
    return farenheit
print('Celsius To Farenheit->')
farenheit=int(input('Enter Temp:'))
print(celsiustofarenheit(farenheit))

def farenheittocelsius(celsius):
    assert(celsius>=0)
    celsius = 5/9*(farenheit-32)
    return celsius
print('Farenheit To Celsius->')
celsius = int(input('Enter Temp:'))
print(farenheittocelsius(celsius))'''






