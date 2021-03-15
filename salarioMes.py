#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


horaTrabalho = float(input('Digite o valor da sua hora de trabalho: '))
horasMes = float(input('Digite quantas horas você trabalhou esse mês: '))

salarioMes= float(horaTrabalho*horasMes)

print(f'Seu salário atual é de R${salarioMes}')

