# 2 exercicios em 1 

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale 
# a população do país B,  mantidas as taxas de crescimento.

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

popA=int(input("População do país A: "))
while popA<0:
    popA=int(input("População do país deve ser maior que 0: "))
taxaA=float(input("Taxa de crescimento da cidade A: "))

popB=int(input("População do país B: "))
while popB<0:
    popB=int(input("População do país deve ser maior que 0: "))
taxaB=float(input("Taxa de crescimento da cidade B: "))

ano=0
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA/100) )* popA)
    popB = int((1 + (taxaB/100) )* popB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)






#Crie agora um script que não importa o tamanho ou taxa de crescimento, diga o ano que uma supera a outra cidade ou que isso nunca vai acontecer.
paisA=80000
paisB=200000
ano=0

while paisA<paisB:
    paisA*=1.03
    paisB*=1.015
    ano+=1

print(ano)