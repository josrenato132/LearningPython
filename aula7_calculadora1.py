class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

c = int(input("Digite um número: "))
d = int(input("Digite um número"))
calculadora = Calculadora(c, d)

print("A soma é: " + str(calculadora.soma()))
print("A subtração é: " + str(calculadora.sub()))
print("A multiplicação é: " + str(calculadora.mult()))
print("A divisão é: " + str(calculadora.div()))