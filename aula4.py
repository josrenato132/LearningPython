for n in range(101):
    d = 0
    for x in range(1, n+1):
         if n%x ==0:
             d += 1

    if d == 2:
        print("{} é primo" .format(n))
    else:
        print("{} não é primo" .format(n))


# n = int(input("Digite um número: "))
# d = 0
# for x in range(1, n+1):
#      if n%x ==0:
#          d += 1
#
# if d == 2:
#     print("Esse número é primo")
# else:
#     print("Esse número não é primo")