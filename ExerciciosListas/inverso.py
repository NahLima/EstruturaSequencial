#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

listaNumeros = []
print ('Informe os 10 numeros')

for i in range(10):
    listaNumeros.append(input('Numero '+ str(i+1) + ':\n'))
    listaNumeros.reverse()
print(listaNumeros)

