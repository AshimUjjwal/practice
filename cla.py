class Add:
    x= 5+9*6

a=Add()
print(a.x)





class Arrow:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def detail(self):
        print('My name is ' + self.name)

w=Arrow('Ashim Ujjwal.',22)
w.detail()




class animal:
    def dog(self,eye,leg,size):
        print('Dog takes ',eye*leg*size)

q=animal()
q.dog(2,4,6)

class monkey(animal):
    def jump(self,eye,leg,size):
        print(eye*leg*size)

obj=monkey()
obj.dog(3,5,3)

class gorrila(monkey,animal):
    def jump(self,eye,leg,size):
        print(eye*leg*size)

o=gorrila()
o.jump(2,3,4)




