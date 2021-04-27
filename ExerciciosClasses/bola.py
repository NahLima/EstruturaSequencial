# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class Ball:
    def __init__(self,color="unknown", circumference=0, material="unknown"):
        self.color = color
        self.circumference= circumference
        self.material = material


    def setColor(self):
        change = input('Deseja mudar a cor da atual da bola {}? [s/n]: '.format(self.color))
        change = change[0].lower()

        if change == "s":
            newColor = input('\n Nova Cor: ')
            self.color = newColor

        else:
            print("OK a cor continua {}.".format(self.color))

    def showColor(self):
        print("\n A cor da bola atual é {}".format(self.color))

def main():
    ball01 = Ball("azul", 5, "isopor")

    while True:
        ball01.showColor()
        ball01.setColor()

        again = input("Again? [s/n]")
        again = again[0].lower
        if again == "n":
            break

    ball01.showColor()

main()



