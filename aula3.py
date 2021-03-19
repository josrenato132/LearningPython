
a = int(input("Nota do primeiro bimestre: "))
while a > 10:
    a = int(input("Nota invalida. Digite novamente: "))
b = int(input("Nota do segundo bimestre: "))
while b > 10:
    b = int(input("Nota invalida. Digite novamente: "))
c = int(input("Nota do terceiro bimestre: "))
while c > 10:
    c = int(input("Nota invalida. Digite novamente: "))
d = int(input("Nota do quarto bimestre: "))
while d > 10:
    d = int(input("Nota invalida. Digite novamente: "))
media = (a + b + c + d) / 4
print("Média: {}" .format(media))



# a = int(input("Digite um número:"))
# b = int(input("Digite outro número:"))
# restoa = a % 2
# restob = b % 2
# if restoa == 0 or restob == 0:
#     print("Um dos números é par")
# else:
#     print("Nenhum número é par")
#

# a = int( input("Digite o primeiro valor: "))
# b = int( input("Digite o segundo valor: "))
# c = int(input("Digite o terceiro valor: "))
# if a > b and a > c:
#     print("O maior número é: {maior}" .format(maior=a))
# elif b > c:
#     print("O maior número é: {maior}" .format(maior=b))
# else:
#     print("O maior número é: {maior}" .format(maior=c))
# print("Final do programa")