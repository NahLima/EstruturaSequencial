# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

grauF = float(input('Digite a temperatura em fahrenheit: '))

def convertF (toCelsius):
    return (grauF-32)*5/ 9  
    
print(convertF(grauF))




#Crie uma função que receba uma temperatura em Celsius e chame uma função que converta para Fahrenheit. F = *9C/5 + 32

grauC = float(input('Digite a temperatura em celsius: '))

def convertC(toFahrenheit):
    return (toFahrenheit*9/5) + 32

print(convertC(grauC))

