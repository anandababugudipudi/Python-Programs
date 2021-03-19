class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
    def multiply(self, i):
        self.i = 4*i

class B(A):
    def __init__(self):
        super().__init__()

    def multipl(self, i):
        self.i = 2*1

s = "Anand"
s[0] = "a"
print(s)
