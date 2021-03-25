#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

import getpass

while True:
    login = input('nome do usuário: ')
    senha = getpass.getpass('senha: ')

    if login != senha :
        print("BEM VINDO(A)!")
        break
    else:
        print('Login e senha não podem ser iguais!')
