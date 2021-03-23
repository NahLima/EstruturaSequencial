#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# A = π * R² --> calculo de área --> π (número irracional cujo valor aproximado é 3,14)

valor = float(input('Digite o valor do circulo: '))

pi = 3.14
area = pi * (valor ** 2) # poderia ser tbm area= pi*(valor*valor) 
print(f'Área do circulo é de: {area} ')



