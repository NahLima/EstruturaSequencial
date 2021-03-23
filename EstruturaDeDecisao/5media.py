#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.




notasLista = []

while True:
    notas = int(input('Coloque suas notas aqui (digite 0 se acabou): '))
    if notas == 0 :
        break
    notasLista.append(notas)
for suasNotas in notasLista:
    print(suasNotas)

qtdNotas = len(notasLista)
entradasNotas = sum(notasLista) 
mediaNota = entradasNotas/qtdNotas

if mediaNota >= 7 :
    print(f'APROVADO! \n sua média foi {mediaNota}')
elif mediaNota == 10 :
    print(f'APROVADO! \n sua média foi {mediaNota}')
elif mediaNota < 7:
    print(f'REPROVADO! \n sua média foi de {mediaNota}')
else:
    print('error')




