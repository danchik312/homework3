class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для пополнения счета: "))
        self.balance += amount
        print("Операция выполнена успешно. \nНовый баланс:", self.balance)

    def kill(self):
        self.balance = 0
        print("Баланс обнулен.")

    def _jackpot(self):
        self.balance *= 10
        print("Выигран джекпот! Новый баланс:", self.balance)

    def merge_balance(self, other):
        other_balance = other.balance
        self.balance += other_balance
        print(f"Новый баланс: {self.balance}")

client1 = Bank("Клиент 1", 100)
client2 = Bank("Клиент 2", 200)

print("Баланс Клиента 1:", client1.balance)
print("Баланс Клиента 2:", client2.balance)

client1.merge_balance(client2)

print("Баланс Клиента 1 после объединения:", client1.balance)
print("Баланс Клиента 2 после объединения:", client2.balance)

client1.moneyX()

def calculator(num1, op, num2):
    """Калькулятор считает"""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "нельзя поделить яблоко на ничто"
    elif op == '**':
        return num1 ** num2
    elif op == '%':
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 % num2
        else:
            return "Только с целыми числами!"
    else:
        return "Ты наверное не правильно написал!"

calcunator = (1 / 1)
print(calcunator)
