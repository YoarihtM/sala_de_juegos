from Juegos import tictactoe
from Juegos import buscaminas
from Juegos import memoria
import random

class Menu:
    selec_juego = 0

    def __init__(self):
        print('\t\t¡Bienvenido a la sala de juegos!')
        self.__elegirJuego()
    
    def __elegirJuego(self):
        self.__elec = input('\tSelecciona uno de los juegos disponibles\n\n1) Tic-Tac-Toe\n2) Buscaminas\n3) Memoria\n4) Salir\n\n')
        self.selec_juego = int(self.__elec)
        
        while self.selec_juego != 4:
            if self.selec_juego == 1:
                ttt = tictactoe.Tictactoe()

                self.flag = self.__primerTiro()

                if self.flag == 1:
                    print('Inicia el Jugador\n')
                    while ttt.revisarTablero():
                        x, y = self.recibirCasilla()
                        ttt.tirar(x, y)
                        if ttt.revisarTablero() == False:
                            break
                        ttt.tiroMaquina()
                else:
                    print('Inicia la Máquina\n')

                    while ttt.revisarTablero():
                        ttt.tiroMaquina()
                        if ttt.revisarTablero() == False:
                            break
                        x, y = self.recibirCasilla()
                        ttt.tirar(x, y)
                break
            elif self.selec_juego == 2:
                bm = buscaminas.Buscaminas()
                break
            elif self.selec_juego == 3:
                memo = memoria.Memoria()

                while memo.revisarTablero():
                    print()
                    memo.tirar()
                    memo.tiroMaquina()

                    print('\t\tPuntos del jugador\t\t\tPuntos de la Maquina')
                    self.pJ = memo.getPuntosJ()
                    self.pM = memo.getPuntosM()
                    print('', end='\t\t\t')
                    print(self.pJ, end='\t\t\t\t\t')
                    print(self.pM)
                
                if self.pJ > self.pM:
                    print('Fin del juego, gana Jugador')
                elif self.pj < self.pM:
                    print('Fin del juego, gana Maquina')
                else:
                    print('Fin del juego, tablas')
                break
            else:
                print('\tRespuesta no válida, vuelve a intentar')
                self.__elegirJuego()
    
    def __primerTiro(self):
        self.prob = random.random()

        if self.prob < 0.5:
            return 0
        else:
            return 1

    def recibirCasilla(self):
        x = input('Ingresa la columna en la que deseas realizar tu tiro: ')
        y = input('Ingresa la columna en la que deseas realizar tu tiro: ')

        return x, y