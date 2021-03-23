
'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''


convIR = 11/100  #0.11
convInss = 8/100 #0.08
convSindicato = 5/100 #0.05

horaTrabalho = float(input('Digite o valor da sua hora de trabalho: '))
horasMes = float(input('Digite quantas horas você trabalhou esse mês: '))

salarioBruto= float(horaTrabalho*horasMes)

pgtoIR = salarioBruto * convIR
pgtoINSS = salarioBruto  * convInss
pgtoSindicato = salarioBruto * convSindicato
somaImpostos = pgtoIR + pgtoINSS + pgtoSindicato

liquido = salarioBruto - somaImpostos

print('Calculos dos descontos')
print(f'+ Salário Bruto: R${salarioBruto}')
print(f'- IR (11%): R${pgtoIR}')
print(f'- INSS (8%): R${pgtoINSS}')
print(f'- Sindicato (5%): R${pgtoSindicato}')
print(f'= Salário líquido: R${liquido}')









