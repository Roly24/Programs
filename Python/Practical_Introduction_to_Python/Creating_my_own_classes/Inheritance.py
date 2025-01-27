class Parent:
    def __init__(self, a):
        self.a = a

    def method1(self):
        return self.a*2
    
    def method2(self):
        return self.a + '!!!'

class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def method1(self):
        return self.a*7
    
    def method3(self):
        return self.a + self.b

p = Parent('hi')
c = Child('hi ', 'bye')

print('Parent method 1:', p.method1())
print('Parent method 2:', p.method2())
print()
print('Child method 1:', c.method1())
print('Child method 2:', c.method2())
print('Child method 3:', c.method3())
