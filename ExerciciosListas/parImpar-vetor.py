#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


par=[]
impar=[]

for i in range (0,20):
    numeros=int(input('Digite os números: '))

    if numeros % 2 == 0 :
        par.append(numeros)

    else :
        impar.append(numeros)


print(f'Numeros pares: {par}')
print(f'Numeros impar: {impar}')



# outra forma de fazer 

vetor = []
PAR = []
IMPAR = []

for numero in range(0, 20):
    vetor.append(int(input("Digite um nÃºmero: ")))

for numero in range(0, 20):
    if vetor[numero] % 2 == 0:
        PAR.append(vetor[numero])
    else:
        IMPAR.append(vetor[numero])

print("Vetor com 20 elementos: " + str(vetor))
print("Vetor com elementos pares: " + str(PAR))
print("Vetor com elementos Ã­mpares: " + str(IMPAR))


