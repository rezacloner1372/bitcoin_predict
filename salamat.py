class school:
    count = 0
    def __init__ (self,number, age, height, weigh):
        self.number = number
        self.age = age
        self.height = height
        self.weigh = weigh
    def from_input(cls):
        return cls(
            input('enter number, age, height, weigh : '),
        )

    def average_age_(self):
        sum_num = 0
        for t in self.age:
            sum_num = sum_num + t
        avg = sum_num / len(self.age)
        return avg
    def average_height(self):
        sum_num = 0
        for t in self.height:
            sum_num = sum_num + t
        avg = sum_num / len(self.height)
        return avg
    def average_weigh(self):
        sum_num = 0
        for t in self.weigh:
            sum_num = sum_num + t
        avg = sum_num / len(self.weigh)
        return avg

class deff(school):
    def value(self):
        if (A.average_height()>B.average_height()):
            print('A')
        else:
            print('B')
        if (A.average_height() == B.average_height()):
            if (A.average_weigh() < B.average_weigh()):
                print('A')
            else:
                print('B')
        if (A.average_height() == B.average_height()) and (A.average_height() == B.average_height()):
            print('Same')


A = school.from_input()
B = school.from_input()

#A = school([6], [16, 17, 15, 16, 17, 14], [180, 175, 177, 170, 165], [67, 72, 59, 62, 55])
#B = school([6], [15, 17, 16, 15, 16, 15], [200, 162, 168, 170, 162], [45, 52, 56, 58, 47])
#A = school(input('enter number, age, height, weigh : '))
#B = school(input('enter number, age, height, weigh : '))
print(A.number[0])
print(A.average_age_())
print(A.average_height())
print(A.average_weigh())
print(A.number[0])
print(B.average_age_())
print(B.average_height())
print(B.average_weigh())
deff.value(school)