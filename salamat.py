class school:
    count = 0
    def __init__ (self,number, age, height, weigh):
        self.number = number
        self.age = age
        self.height = height
        self.weigh = weigh
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
    def deff(self):
        if A.average_height()>B.average_height():
            return 'A'
        else:
            return 'B'


A = school([5], [16, 17, 15, 16, 17], [180, 175, 172, 170, 165], [67, 72, 59, 62, 55])
B = school([5], [15, 17, 16, 15, 16], [166, 156, 168, 170, 162], [45, 52, 56, 58, 47])
print(A.number)
print(A.average_age_())
print(A.average_height())
print(A.average_weigh())
print(B.average_age_())
print(B.average_height())
print(B.average_weigh())
print(deff)