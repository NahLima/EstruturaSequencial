import math

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


#Coisas que você precisa saber antes de começar:
# Produto é o resultado de uma multiplicação ;D
# Numero real é aquele que pode ser inteiro ou decimal, positivo ou negativo…

firstNum = int(input('Digite o primeiro número inteiro: '))
secondNum = int(input('Digite o segundo número inteiro: '))
realNum = float(input('Digite o numero real: '))

resp1 = firstNum *2*(secondNum/2)
print(f'O produto do dobro do primeiro com metade do segundo: {resp1} ')

resp2 = firstNum * 3 + realNum
print(f'A soma do triplo do primeiro com o terceiro: {resp2}')

resp3 = realNum ** 3
print(f'O terceiro elevado ao cubo: {resp3}')

