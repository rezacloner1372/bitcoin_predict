class Copmuter:
    count = 0
    def __init__(self,ram,hard,cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram+self.hard+self.cpu

class Laptop(Copmuter):
    def value(self):
        return self.ram+self.hard+self.cpu+self.size



pc1 = Copmuter(12,2,4)
print(pc1.value())

laptop1 = Laptop(4,2,1)
laptop1.size = 13
print(laptop1.value())