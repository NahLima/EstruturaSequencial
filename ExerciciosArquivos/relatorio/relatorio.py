import os

# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco
# no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede
# precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
# Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
# gere um relatório, chamado "relatório.txt", no seguinte formato:

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
# deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual
# de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.



arquivo = "usuarios.txt"


def bytes_to_mb(qtdBytes):
    return str(round(qtdBytes/1048576, 2)).replace('.', ',')


def percent(spaceUser, total):
    return str(round(spaceUser*100/total, 2)).replace('.', ',')


if os.path.exists(arquivo):

    userSpaceTxt = open(arquivo, "r")
    usersSpaces = userSpaceTxt.read().split("\n")

    if len(usersSpaces) > 0:
        arquivo_relatorio = open("relatorio.txt", "wt")
        arquivo_relatorio.write( "ACME Inc.               Uso do espaço em disco pelos usuários\n")
        arquivo_relatorio.write("-" * 72 + "/n")

        arquivo_relatorio.write("Nr.".ljust(5))
        arquivo_relatorio.write("User".ljust(15))
        arquivo_relatorio.write("Used_Space".ljust(21))
        arquivo_relatorio.write("Percent %".ljust(9) + "\n\n")

        totalSpace = 0

        for userSpace in usersSpaces:
            totalSpace += int(userSpace.split()[1])

        for index_user_espace in range(len(usersSpaces)):
            userSpace = usersSpaces[index_user_espace].split()

            user = userSpace[0]
            space = userSpace[1]

            arquivo_relatorio.write(str(index_user_espace+1).ljust(5))
            arquivo_relatorio.write(user.ljust(15))
            arquivo_relatorio.write(bytes_to_mb(int(space)).rjust(7)+" MB           ")   
            arquivo_relatorio.write(percent(int(space), totalSpace).rjust(7)+"%/n")
                

        arquivo_relatorio.write(
            "\nEspaco total ocupado: " + bytes_to_mb(totalSpace) + "MB\n")
        arquivo_relatorio.write(
            "Espaco médio ocupado: " + bytes_to_mb(totalSpace/len(usersSpaces)) + "MB")

        arquivo_relatorio.close()

else:
    print("O arquivo não existe")
