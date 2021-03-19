contaLetras = lambda lista: [len(x) for x in lista ]

list = ["Animal", "Outro"]
print(contaLetras(list))

calculadora = {
    "soma" : lambda a, b: a+b,
    "sub" : lambda a,b : a-b,
    "mult" : lambda a,b : a*b,
    "div" : lambda a,b: a/b,
}

soma = calculadora["soma"]
print("A soma é: {}".format(soma(5,10)))