class Calculadora:
    def __init__(self):
        pass
    def ad(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

c = int(input("Type a number: "))
d = int(input("Type another number: "))
calc = Calculadora()

print("Addition: {}" .format(calc.ad(c, d)))
print("Subtraction: {}" .format(calc.sub(c, d)))
print("Multiplication: {}" .format(calc.mult(c, d)))
print("Division: {}" .format(calc.div(c, d)))