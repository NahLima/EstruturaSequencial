
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letras = input('Digite sua letra aqui: ').lower()

vogal = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z']

def alfabeto(entradaUser):
    if letras == entradaUser in vogal:
        return 'A letra digitada é vogal!'
    elif letras == entradaUser in consoantes:
        return 'A letra digitada é consoante!'
    else:
        return 'error'
   
print(alfabeto(letras))

