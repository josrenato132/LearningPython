a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = a + b
sub =  a - b
mult = a * b
div = a / b
media = (a + b) / 2;
resto = a % b
print ("A soma é: {soma}. \n A subtração é: {sub}. \n A multiplicação é: {mult}. \n A divisão é: {div}. \n O resto da divisão é: {resto}. \n A média é: {media}" .format(soma=soma, sub=sub, mult=mult, div=div, resto=resto, media=media))
