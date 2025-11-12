class Person:
    def __init__(self, name):
        self.name = name

    def data(self):
        print(f'{self.name} is 32 years old.')


class Driver_1(Person):
    def __init__(self, name, number_driving_lic):
        super().__init__(name)
        self.number_driving_lic = number_driving_lic
        print(f'{self.name}\'s number of driving license is {self.number_driving_lic}')


class Driver_2(Person):
    def __init__(self, name, number_driving_lic, car):
        super().__init__(name)
        self.number_driving_lic = number_driving_lic
        self.car = car
        print(f'{self.name}\'s number of driving license is {self.number_driving_lic}')
        print(f'{self.name}\'s car is {self.car}')


info_1 = Driver_1('Tom','FD 053682375')
info_1.data()

info_2 = Driver_2('Ann', 'FD 053682375', 'BMW')
info_2.data()
