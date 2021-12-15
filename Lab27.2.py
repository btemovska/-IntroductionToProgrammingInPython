class Calculator:
    # Type your code here.
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value = self.value + val
    def subtract(self, val):
        self.value = self.value - val
    def multiply(self, val):
        self.value = self.value * val
    def divide(self, val):
        self.value = self.value / val

    def clear(self):
        self.value = 0

    def get_value(self):
        return self.value


if __name__ == "__main__":
    calc = Calculator()
    num1 = float(input())
    num2 = float(input())

    # 1. The initial value
    print('{:.1f}'.format(calc.get_value()))

    calc.add(num1)
    print('Add {:.1f}'.format(calc.get_value()))

    calc.multiply(3)
    print('Multiply by 3 - {:.1f}'.format(calc.get_value()))

    calc.subtract(num2)
    print('Subtract {:.1f}'.format(calc.get_value()))

    calc.divide(2)
    print('Divide by 2 {:.1f}'.format(calc.get_value()))

    calc.clear()
    print('{:.1f}'.format(calc.get_value()))
