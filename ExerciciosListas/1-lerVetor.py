#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = [1,3,6,8,9]
print(vetor)

# com while
vetorList = [1, 4, 9, 22, 18]

i = 0
while i < len(vetorList):
    print(vetorList[i])
    i = i + 1

#com for
listaNumeros = []
print ('Informe os 5 numeros')

for i in range(5):
    listaNumeros.append(input('Numero '+ str(i+1) + ':\n'))
print (listaNumeros) 




