#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.


listaInput = []
consoantes = 0
vogal = 0
print ('Informe os caracters')

for i in range(10):
	lista = input('Coloque as letras aqui: ')
	listaInput.append(lista)

	characters = listaInput[i]
    	
	if (characters not in ('a','e','i','o','u' )):
		consoantes+=1
	
print(listaInput)
print(f'Existem {consoantes} consoantes nesta lista') # contagem de consoantes

	




