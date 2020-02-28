tabuleiroPadrao = [
                    " "," "," ",
                    " "," "," ",
                    " "," "," "
                    ]

class Partida():
    def __init__(self):
        self.tabuleiro = tabuleiroPadrao
        self.turno = "jogador1"
        self.jogador1 = "jogador1"
        self.jogador2 = "jogador2"


def showTable(p1):
    print("  A" + " " + "B" + " " + "C")
    print("1 "+p1.tabuleiro[0] + "|"+ p1.tabuleiro[1]+"|"+ p1.tabuleiro[2])
    print("2 "+p1.tabuleiro[3] + "|"+ p1.tabuleiro[4]+"|"+ p1.tabuleiro[5])
    print("3 "+p1.tabuleiro[6] + "|"+ p1.tabuleiro[7]+"|"+ p1.tabuleiro[8])
    print("")
    print('Press 1 = A1, 2 = B1, 3 = C1, 4 = A2, 5 = B2, 6 = C2, 7 = A3, 8 = B3, 9 = C3') 
    x = input('Enter your choise:')
def main():
    p1 = Partida()
    showTable(p1)

if __name__ == "__main__":
   main()