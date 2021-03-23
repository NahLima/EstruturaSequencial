import math

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite a sua altura: '))

def calculo (pesoIdeal):
    return (72.7 * altura) - 58
print( 'seu peso ideal é:')
print(calculo(altura))


# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Digite a sua altura: '))

mulher = round((62.1*h) - 44.7, 2)
homem = round((72.7*h) - 58 , 2)

print(f'Peso ideal para homens: {homem}')
print(f'Peso ideal para homens: {mulher}')


