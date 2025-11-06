import random

class Need:
    def __init__(self, name, value=100):
        self.name = name
        self.value = value

    def add(self, x):
        self.value = min(100, self.value + x)

    def sub(self, x):
        self.value = max(0, self.value - x)

    def __str__(self):
        return f"{self.name}: {self.value}"


class Phone:
    def __init__(self):
        self.battery = Need("Заряд телефону", 100)

    def use(self, amount):
        self.battery.sub(amount)

    def charge(self):
        print("Телефон заряджається 🔌")
        self.battery.add(30)


class Sim:
    def __init__(self, name):
        self.name = name
        self.energy = Need("Енергія", 80)
        self.hunger = Need("Голод", 20)
        self.mood = Need("Настрій", 80)
        self.phone = Phone()
        self.alive = True

    def eat(self):
        print(f"{self.name} їсть 🍎")
        self.hunger.sub(30)
        self.energy.add(10)
        self.mood.add(5)
        self.phone.use(10)

    def sleep(self):
        print(f"{self.name} спить 😴")
        self.energy.add(40)
        self.hunger.add(10)
        self.phone.use(5)

    def play(self):
        print(f"{self.name} грається 🎮")
        self.mood.add(20)
        self.energy.sub(10)
        self.hunger.add(10)
        self.phone.use(20)

    def work(self):
        print(f"{self.name} працює 💼")
        self.energy.sub(20)
        self.mood.sub(15)
        self.hunger.add(20)
        self.phone.use(20)

    def charge_phone(self):
        self.phone.charge()

    def show_status(self):
        print(f"\n=== {self.name} ===")
        print(self.energy)
        print(self.hunger)
        print(self.mood)
        print(self.phone.battery)
        print("==================")

    def update(self):
        self.energy.sub(random.randint(0, 5))
        self.hunger.add(random.randint(0, 5))
        self.mood.sub(random.randint(0, 3))
        self.phone.use(random.randint(0, 5))
        if self.energy.value == 0 or self.hunger.value == 100 or self.mood.value == 0 or self.phone.battery.value == 0:
            self.alive = False


def main():
    name = input("Введи ім’я персонажа: ")
    sim = Sim(name)

    while sim.alive:
        sim.show_status()
        print("\n1 - Їсти 🍎")
        print("2 - Спати 😴")
        print("3 - Грати 🎮")
        print("4 - Працювати 💼")
        print("5 - Зарядити телефон 📱")
        print("0 - Вийти 🚪")

        action = input(">> ")

        if action == "0":
            print("До зустрічі!")
            break
        elif action == "1":
            sim.eat()
        elif action == "2":
            sim.sleep()
        elif action == "3":
            sim.play()
        elif action == "4":
            sim.work()
        elif action == "5":
            sim.charge_phone()
        else:
            print("Невідома команда!")

        sim.update()

    if not sim.alive:
        sim.show_status()
        print(f"\n{sim.name}, схоже щось пішло не так... Гра закінчена!")

main()