#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Informe o tamanho do arquivo para donwload (em MB): '))
velocidade = float(input('Informe a velocidade de sua internet (em MBPS): '))

def calculo():
    tempo = arquivo / velocidade
    minuto = round(tempo / 60.0, 2)
    return minuto

#print('O tempo aproximado para download do arquivo usando este link e de: ' calculo(duracao))

