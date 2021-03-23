#Faça um Programa que peça dois números e imprima o maior deles

numeroUm=int(input('Digite o primeiro número: '))
numeroDois=int(input('Digite o segundo número: '))

if numeroUm > numeroDois:
    print(numeroUm)
elif numeroDois > numeroUm:
    print(numeroDois)
elif numeroUm == numeroDois or numeroDois == numeroUm:
    print('Numeros iguais')
else:
    print('error')
