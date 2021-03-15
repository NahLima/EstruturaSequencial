
#Faça um Programa que converta metros para centímetros.

print('conversor de metros para centimetros /n')

metros=int(input('Digite o número metro : '))
centimetros = int(input('Digite o número cm : '))


convMetro = metros*100
somaCm = convMetro+centimetros


print("Conversão realizada com sucesso!")
print(f"O valor convertido é:{somaCm} ")



#Programa que leia um valor INTEIRO de metros e converta em centímetros e milímetros.
metros = float(input('Digite a quantidade de metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('valores convertidos com sucesso!')

print(f'centimetros = {centimetros} cm, milimetros = {milimetros} mm')


#Faça um Programa que converta km para metros.
numeroKm = float(input('Digite a quantidade de metros: '))

convKm = numeroKm/1000


print('valores convertidos com sucesso!')

print(f'km convertidos em metros: {convKm}')

