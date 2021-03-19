conjunto = {1, 2, 3, 4}
conjunto2 = {4, 5, 6, 7}
conjuntoIntersec = conjunto.intersection(conjunto2)
conjuntoUniao = conjunto.union(conjunto2)
conjuntoDiferenca = conjunto.difference(conjunto2)
conjuntoDiferenca2 = conjunto2.difference(conjunto)
# conjunto.add(1)
# conjunto.discard(1)
print("Conjunto 1: {}".format(conjunto))
print("Conjunto 2: {}".format(conjunto2))
print("União: {}".format(conjuntoUniao))
print("Intersec: {}".format(conjuntoIntersec))
print("Diferença de 1 pra 2: {}".format(conjuntoDiferenca))
print("Diferença de 2 pra 1: {}".format(conjuntoDiferenca2))
