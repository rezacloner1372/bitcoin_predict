class mobile:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def get_name(self):
        return self.name


class cpu(mobile):
    def get_name(self):
        print("This mobile has HighTech %s CPU" % self.name)


brand = cpu("Intel", "Sony")
print(brand.get_name())