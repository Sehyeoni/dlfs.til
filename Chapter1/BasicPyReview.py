print(1 + 2)

# type()
print(type(10))
print(type(2.718))
print(type("hi"))

# variable
v = 1
print(v)

# list
l = ['a', 'b', 'c', 'd', 'e']
print(l)
print(type(l))

# dictionary
d = {'apple': 3000, 'banana': 1000}
print(d['apple'])

d['kiwi'] = 5000
print(d)

# bool
b1 = True
b2 = False
print(b1)
print(type(b2))
print(b1 and b2)
print(b1 or b2)

# if
if b1:
    print("b1 is True")
else:
    print("This is not True")

# for
for i in [1, 2, 3]:
    print(i)


# function
def hello(name):
    print("hello " + name)


hello('su')

# class
class Icecream:
    def __init__(self, name):
        self.name = name
        print(self.name + ' initialized')

    def name(self):
        print(self.name)


icecream = Icecream('Strawberry')
icecream.name()