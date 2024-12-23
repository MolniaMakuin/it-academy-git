class PlayStation:
    def __init__(self, console, number_of_consoles, controllers, games, material):
        self.console = console
        self.number_of_consoles = number_of_consoles
        self.controllers = controllers
        self.games = games
        self.material = material

    def __str__(self):
        return (f'console - {self.console}, number_of_console - {self.number_of_consoles}, '
                f'controller - {self.controllers}, game - {self.games}, material - {self.material}')

    def __sub__(self, other):
        return 5 - other

    def __rsub__(self, other):
        return other - 2

    def __gt__(self, other):
        return self.controllers > other.controllers

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.number_of_consoles + other

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return other + self.number_of_consoles

    def __bool__(self):
        if self.number_of_consoles >= 20:
            return True
        else:
            return False


class PS5(PlayStation):
    def __sub__(self, other):
        return 5 - other

    def __rsub__(self, other):
        return other - 2

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.number_of_consoles + other

    def __bool__(self):
        if self.number_of_consoles >= 20:
            return True
        else:
            return False

info_PlayStation = PlayStation('PS5', 5, 'DualSense', 'The Long Dark', 'Chroma Teal')
print(info_PlayStation)
result = 5 > 20
print(result)
print(f'{info_PlayStation - 1} Осталось консолей')
print(f'{info_PlayStation + 3.5} Добавили консоли в магазин')


class PS5Pro(PlayStation):
    def __sub__(self, other):
        return 5 - other

    def __rsub__(self, other):
        return other - 2

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return other + self.number_of_consoles

info_PlayStation2 = PlayStation('PS5 Pro', 9, 'DualSenseEdge', 'Spider-Man', 'Midnight Black')
print(info_PlayStation2)
print(f'{9 - info_PlayStation2} Осталось консолей')
print(f'{2 + info_PlayStation} Добавили консоли в магазин')
print(info_PlayStation.controllers > info_PlayStation2.controllers)
if info_PlayStation > info_PlayStation2:
    print(f'{info_PlayStation.controllers} хуже чем {info_PlayStation2.controllers}')
else:
    print(f'{info_PlayStation2.controllers} лучше чем {info_PlayStation.controllers}')


class Console:
    def __get__(self, instance, owner):
        if instance.has_playstation:
            return instance.playstation_console

        return 'Приставки нет'

    def __set__(self, instance, value):
        if not instance.has_playstation:
            instance.playstation_console = value
            instance.has_playstation = True

            print('Приставка куплена')

            return

        print('У тебя есть приставка')

    def __delete__(self, instance):
        print('Отдать приставку')
        del instance.playstation_console
        instance.has_playstation = False


class Client:
    playstation = Console()

    def __init__(self, name, has_playstation=False):
        self.name = name
        self.has_playstation = has_playstation

    def get_name(self):
        return f'Name - {self.name}'

Yana = Client('Yana')
print(Yana.playstation)
Yana.playstation = 'PS5'
Yana.playstation = 'PS5 Pro'
print(Yana.playstation)
del Yana.playstation
print(Yana.playstation)


class BankAccount:
    def __init__(self, name, balance, purchase):
        self.name = name
        self.__balance = balance
        self.purchase = purchase

    def __str__(self):
        return f'{self.name} - {self.purchase}, balance - {self.__balance}'

    def deposit(self, amount):
        self.__balance += amount

    def deposit_minus(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __sub__(self, other):
        return 3800 - other

    def __abs__(self):
        return -100

client1 = BankAccount('Yana', 3000, 'PS5')
print(client1)
client1.deposit(900)
print(f'{client1.get_balance()} Сумма на балансе')
client1.deposit_minus(100)
print(f'{client1.get_balance()} Сумма на балансе')
print(client1 - 3900)
print(abs(-100))