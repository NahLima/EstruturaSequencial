import math

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.print
# 'Calculo para verificar quantas latas/galões de tintas serão necessarias e o valor delas'

metros = int(
    input("Entre com o tamanho em metros quadrados da área a ser pintada: "))

metrosLatas = metros / 6
if (metrosLatas <= 0):
    metrosLatas = 1


qtdLatas18 = math.floor(metrosLatas / 18+(18*0.10))
qtdGaloes36 = math.floor(metrosLatas / 3.6+(3.6*0.10))
qtdLatas = metrosLatas / 18
resto = metrosLatas % 18

if (resto > 0 and resto <= 3.6):
    qtdGaloes = 1
elif (resto == 0):
    qtdGaloes36 = 0
else:
    qtdGaloes = math.floor(resto / 3.6+(3.6*0.10))

if (qtdLatas18 <= 0 or qtdGaloes36 <= 0 or qtdGaloes < 0):
    qtdGaloes36 = 1
    qtdLatas18 = 1
    qtdGaloes = 1

precoLatas18 = qtdLatas18 * 80
precoGaloes36 = qtdGaloes36 * 25
precoLatas = qtdLatas * 80
precoGaloes = qtdGaloes * 25

otimoPreco = precoLatas + precoGaloes


print('\n Quantidade de latas: %d latas. Preço latas: %.2f reais. \n Quantidades galões: %d galões. Preço galões: %.2f. \n Melhor custo, latas: %d e galões: %d Valor:%.2f' %
      (qtdLatas18, precoLatas18, qtdGaloes36, precoGaloes36, qtdLatas, qtdGaloes, otimoPreco))

